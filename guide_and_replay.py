import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm
import time

if __name__ == "__main__":
    print('Starting robot')
    fa = FrankaArm()
    
    print('Resetting Arm')
    fa.reset_joints()

    guideTime = 10 #seconds
    done = False
    jointsLoc1 = []
    while not done:
        print("Franka in guide mode for {} seconds".format(guideTime))
        print("\tPlace gripper stradling target cup edge")
        fa.run_guide_mode(guideTime, block=True)
        
        inp = input("If you are satisfied with the current position type 'y':")
        if inp == "y":
            print("Recording joints position")
            done = True
            jointsLoc1 = fa.get_joints()
        else:
            print("Trying again")
            # time.sleep(1)
    print("First recorded joint position: {}".format(jointsLoc1))

    print("Resetting arm")
    fa.reset_joints()

    jointsLoc2 = []
    done = False
    while not done:
        print("Franka in guide mode for {} seconds".format(guideTime))
        print("\tMove robot arm above center of second cup")
        fa.run_guide_mode(guideTime, block=True)
        
        inp = input("If you are satisfied with the current position type 'y':")
        if inp == "y":
            print("Recording joints position")
            done = True
            jointsLoc2 = fa.get_joints()
        else:
            print("Trying again")
            # time.sleep(1)
    print("Second recorded joint position: {}".format(jointsLoc2))

    print("Resetting arm")
    fa.reset_joints()

    print("Going to first joint position")
    fa.goto_joints(jointsLoc1)
    fa.close_gripper()

    print("Resetting")
    fa.reset_joints()

    print("Going to second joint position")
    fa.goto_joints(jointsLoc2)
