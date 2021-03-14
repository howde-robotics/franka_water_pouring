import numpy as np
from utils import *


class FrankaEmika:

    def __init__(self):
        # joint number
        self.jointNum = 7

        # RPY, XYZ for each link
        self.urdfParams = np.array([[    0, 0, 0,       0,      0, 0.333],
                                 [-np.pi/2, 0, 0,       0,      0,     0],
                                 [ np.pi/2, 0, 0,       0, -0.316,     0],
                                 [ np.pi/2, 0, 0,  0.0825,      0,     0],
                                 [-np.pi/2, 0, 0, -0.0825,  0.384,     0],
                                 [ np.pi/2, 0, 0,       0,      0,     0], 
                                 [ np.pi/2, 0, 0,   0.088,      0,     0],
                                 [       0, 0, 0,       0,      0, 0.107]])

        # array of link transforms
        self.LinkTransforms = np.zeros((4, 4, self.jointNum))


    def forward(self):
        for i in range(self.jointNum):
            self.urdfParams[i]


if __name__ == "__main__":
    robot = FrankaEmika()
    robot.forward()