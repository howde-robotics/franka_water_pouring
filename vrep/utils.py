import numpy as np


def homogTrans(rpy, XYZ):
    homogTrans, homogRoll, homogPitch, homogYaw = np.eye(4), np.eye(4), np.eye(4), np.eye(4)
    

    homog = homogTrans @ homogYaw @ homogPitch @ homogRoll

    return homog