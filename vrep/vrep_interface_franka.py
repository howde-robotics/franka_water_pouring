import vrep
import time
import numpy as np


class vrepBot:

	def __init__(self):
		self.totalJoints = 7
		self.clientID = None
		self.JointHandles = None
		self.GripperHandles = None
		
		
	def connect(self):
		'''
		connect to the VREP simulation
		'''

		vrep.simxFinish(-1) # just in case, close all opened connections
		self.clientID=vrep.simxStart('127.0.0.1', 19997,True,True,5000,5) # Connect to V-REP		
		if self.clientID==-1:
			print('Failed connecting to remote API server')
			exit()

		#Start simulation and enter sync mode
		vrep.simxSynchronous(self.clientID,True)
		vrep.simxStartSimulation(self.clientID,vrep.simx_opmode_oneshot)

		# Create connections to joints and sensors
		FrankaJointName = "Franka_joint"

		self.JointHandles=[vrep.simxGetObjectHandle(self.clientID,FrankaJointName+str(jointNum + 1),vrep.simx_opmode_blocking)[1] for jointNum in range(self.totalJoints)]

		# get the gripper handle
		self.GripperHandles = vrep.simxGetObjectHandle(self.clientID, "RG2_openCloseJoint", vrep.simx_opmode_blocking)[1]

		#Start Streaming buffers
		JointPosition=[vrep.simxGetJointPosition(self.clientID, JointHandle,vrep.simx_opmode_streaming)[1] for JointHandle in self.JointHandles]

	def shutdown(self):
		'''
		Shut off the robot
		'''
		vrep.simxStopSimulation(self.clientID,vrep.simx_opmode_blocking)
		vrep.simxFinish(self.clientID)



	def getJointPos(self):
		''' 
		Return the joint positions
		'''
		CurJointPosition=[vrep.simxGetJointPosition(self.clientID, JointHandle,vrep.simx_opmode_buffer)[1] for JointHandle in self.JointHandles]
		return CurJointPosition
	

	def move(self, DesJointPosition):
		'''
		Move robot to current joint positions
		'''
		CurJointPosition=self.getJointPos()
		for i in range(15):
			t=min(i,12.)/12.
			vrep.simxPauseCommunication(self.clientID,1)
			for j in range(5):
				vrep.simxSetJointTargetPosition(self.clientID,self.JointHandles[j], (1.0-t)*CurJointPosition[j]+t*DesJointPosition[j],vrep.simx_opmode_oneshot)
			vrep.simxPauseCommunication(self.clientID,0)
			for step in range(3):
				vrep.simxSynchronousTrigger(self.clientID)

			print(self.getJointPos())

	def reset_joints(self):
		'''
		Tells the Franka to go home from whereever it is.
		'''
		curPos = self.getJointPos()
		print("Going home from: ", curPos)
		homePos=[0,0,0,0,-np.pi/2,0,np.pi/2]

		self.move(homePos)

	def close_gripper(self):
		# doesn't work yet
		gripPos = vrep.simxGetJointPosition(self.clientID, self.GripperHandles, vrep.simx_opmode_oneshot)[0]
		print(gripPos)

		vrep.simxSetJointTargetVelocity(self.clientID, self.GripperHandles, -0.05, vrep.simx_opmode_oneshot)
		print(gripPos)
		

	def open_gripper(self):
		pass


	def get_pose(self):
		curJoints = self.getJointPos()

			
	       




