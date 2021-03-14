import vrep_interface_franka as vpi
import time
import numpy as np

robot=vpi.vBot()

robot.connect()

robot.move([0.2, 0, 0, 3, 0, 2, 0])

time.sleep(2)

robot.reset_joints()

time.sleep(2)

robot.shutdown()



