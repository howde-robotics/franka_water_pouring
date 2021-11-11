import numpy as np
import vrep_interface_franka as vri
from utils import *


class FrankaEmika(vri.vrepBot):
    ''' Franka Emika Panda robot for use with VREP simulation. '''

    def __init__(self):
        # super().__init__()

        # joint number
        self.jointNum = 7

        # RPY, XYZ for each link, last row is for end effector
        self.urdfParams = np.array([[    0, 0, 0,       0,      0, 0.333],
                                 [-np.pi/2, 0, 0,       0,      0,     0],
                                 [ np.pi/2, 0, 0,       0, -0.316,     0],
                                 [ np.pi/2, 0, 0,  0.0825,      0,     0],
                                 [-np.pi/2, 0, 0, -0.0825,  0.384,     0],
                                 [ np.pi/2, 0, 0,       0,      0,     0], 
                                 [ np.pi/2, 0, 0,   0.088,      0,     0],
                                 [       0, 0, 0,       0,      0, 0.107]])

        # array of link transforms
        self.linkTransforms = np.zeros((4, 4, self.jointNum + 1))
        # arrray of joint transforms with empty EE "joint"
        self.jointTransforms = np.zeros((4, 4, self.jointNum + 1))
        # current transforms to everything including EE
        self.currentTransforms = np.zeros((4, 4, self.jointNum + 1))
        # joint angles
        self.jointAngles = np.zeros(self.jointNum + 1)
        self.trueAngles = np.zeros_like(self.jointNum)
        # jacobian matrix
        self.jacobian = np.zeros((6, 7))

        # populate list of link transforms (constant)
        for i in range(self.urdfParams.shape[0]):
            link = self.urdfParams[i]
            self.linkTransforms[:, :, i] = homogTrans(link[0:3], link[3:])
        
        # connect to simulation on initializing
        # self.connect()

    
    # def __del__(self):
        # self.shutdown()


    def forward(self, qVal):
        ''' forward kinematics calculates all the transforms to each joint and the jacobian'''
        self.jointAngles[:-1] = qVal

        for i in range(len(self.jointAngles)):
            q = self.jointAngles[i]

            # joint axis is z for all joints
            self.jointTransforms[:, :, i] = homogTrans([0, 0, q], [0, 0, 0])

            # calcualte all current joint frames
            if i == 0:
                self.currentTransforms[:, :, i] = self.linkTransforms[:, :, i] @ self.jointTransforms[:, :, i]
            
            else:
                self.currentTransforms[:, :, i] = self.currentTransforms[:, :, i - 1] @ self.linkTransforms[:, :, i] @ self.jointTransforms[:, :, i]

        # calculate the jacobian
        for i in range(self.jointNum):
            # distance from end effector to i-th joint
            posOffset = self.currentTransforms[:, :, -1][0:3, 3] - self.currentTransforms[:, :, i][0:3, 3]
            # current z axis of i-th joint
            axis = self.currentTransforms[:, :, i][0:3, 2]
            self.jacobian[0:3, i] = np.cross(axis, posOffset)
            self.jacobian[3:7, i] = axis

        return self.currentTransforms, self.jacobian

    def inverse(self, qStart, transGoal, xEps=1e-3, rEps=1e-3, iterations=10000):
        '''
        performs iterative inverse kinematics to recover the needed joint angles to obtain desired pose
        '''
        self.forward(qStart)

        # position and ori error
        error = np.zeros(6)
        for s in range(iterations):
            # calculate rotation angle Re = Rgoal Rcur'
            rotErrR = transGoal[0:3, 0:3] @ self.currentTransforms[:, :, -1][0:3, 0:3].T
            rErrAxis, rErrAng = matToAxisAng(rotErrR)

            # clamp rotation angle
            if rErrAng > 0.1:
                rErrAng = 0.1
            if rErrAng < -0.1:
                rErrAng = -0.1

            rotationErr = rErrAxis*rErrAng

            # calculate position error
            positionErr = transGoal[0:3, 3] - self.currentTransforms[:, :, -1][0:3, 3]
            # clamp position error
            if np.linalg.norm(positionErr) > 0.01:
                positionErr = positionErr*0.01/np.linalg.norm(positionErr)

            error[0:3] = positionErr
            error[3:6] = rotationErr

            # if norm of the error is below thresholds then exit
            if np.linalg.norm(error[0:3]) <= xEps and np.linalg.norm(error[3:6]) <= rEps:
                break
            
            # update angles with the damped least squares error
            W = np.eye(7)
            C = 1e6 * np.eye(6)

            jacobianDLS = W @ self.jacobian.T @ np.linalg.inv(self.jacobian @ W @ self.jacobian.T + np.linalg.inv(C))
            jacobianDx = jacobianDLS @ error

            self.jointAngles[0:-1] += jacobianDx

            # recompute forward kinematics for new angles
            self.forward(self.jointAngles[0:-1])

        return self.jointAngles[0:-1], error
    
    def get_pose(self):
        self.update_joints()
        self.forward(self.jointAngles)
        return self.currentTransforms[:, :, -1]

    def get_joints(self):
        self.update_joints()
        return self.jointAngles

    def goto_pose(self, goalPose):
        self.inverse(self.jointAngles[:-1], goalPose)
        self.move(self.jointAngles[:-1])
        self.update_joints()

    def update_joints(self):
        self.trueAngles = self.getJointPos()
        self.jointAngles = self.trueAngles


if __name__ == "__main__":
    robot = FrankaEmika()
    robot.forward([0,-np.pi/4,0,-np.pi/2,0,np.pi/4, 0])
    print(robot.currentTransforms[:, :, 6])
    print()
    goal = np.array([[1, 0,  0, 0.75],
                     [0, 0, -1, -0.1], 
                     [0, 1,  0, 0.45],
                     [0, 0,  0,    1]])

    robot.inverse(robot.jointAngles[:-1], goal)
    print(robot.jointAngles)