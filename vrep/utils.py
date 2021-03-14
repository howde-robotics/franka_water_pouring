import numpy as np

def homogTrans(rpy, xyz):
    homogTrans, homogRoll, homogPitch, homogYaw = np.eye(4), np.eye(4), np.eye(4), np.eye(4)
    
    # fill in the information
    homogTrans[0:3, 3] = xyz
    alpha, beta, gamma = rpy
    homogRoll[0:3, 0:3] = [[1,              0,              0],
                           [0,  np.cos(alpha), -np.sin(alpha)], 
                           [0,  np.sin(alpha),  np.cos(alpha)]]
                       
    homogPitch[0:3, 0:3] = [[ np.cos(beta), 0, np.sin(beta)],
                            [            0, 1,            0],
                            [-np.sin(beta), 0, np.cos(beta)], 
                          ]                          
    homogYaw[0:3, 0:3] = [[np.cos(gamma), -np.sin(gamma), 0],
                          [np.sin(gamma),  np.cos(gamma), 0], 
                          [            0,              0, 1]]

    homog = homogTrans @ homogYaw @ homogPitch @ homogRoll

    return homog


def matToAxisAng(R):
    rodR = (R[0, 0] + R[1, 1] + R[2, 2] - 1)/2
    angle = np.arccos(rodR)
    pseudoAxis = np.array([R[2, 1] - R[1, 2], 
                           R[0, 2] - R[2, 0], 
                           R[1, 0] - R[0, 1]])

    Z = np.linalg.norm(pseudoAxis)

    if Z == 0:
        return [1, 0, 0], 0
    
    axis = pseudoAxis / Z
    return axis, angle
