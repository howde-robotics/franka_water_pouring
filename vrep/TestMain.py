import franka_robot as fk
import time
import numpy as np

robot=fk.FrankaEmika()

robot.move([np.pi,-np.pi/4,0,-np.pi/2,0,np.pi/4, 0, 0])
# robot.move(np.zeros(7))

time.sleep(3)

goal = np.array([[1, 0,  0, 0.75],
                 [0, 0, -1, -0.1], 
                 [0, 1,  0, 0.45],
                 [0, 0,  0,    1]])

# robot.goto_pose(goal)

robot.move([-0.076449,    0.74708786,  0.14732362, -1.12714174, -1.6570472,   1.51083392,
  0.29700908])
time.sleep(3)

