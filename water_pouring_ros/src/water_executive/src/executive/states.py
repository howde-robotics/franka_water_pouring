from autolab_core import RigidTransform
from frankapy import FrankaArm
from std_msgs.msg import Bool
import time
import numpy as np
from rrt import rrt

# main franka object
print("[STATES] Starting Robot")
Franka = FrankaArm()


jointFillCup =   np.array([-0.00523853, -0.02406041,  0.00771755, -2.39707949, -0.0693488,   3.73495897,  0.78488679])
jointPourCup =   np.array([ 0.59937575, -0.70281775, -1.05938841, -2.45454394, -0.72683186,  3.53392083, 0.78463731])

eventDict = {
    "GOAL_REACHED"      :False,
    "FILL_WATER_LOW"    :False,
    "SCALE_WATER_LOW"   :False,
    "SCALE_WATER_HIGH"  :False,
    "FILL_WATER_HIGH"   :False,
    "TRAIN"             :False,
    "IDLE"              :False,
    "TRAIN_GRIP"        :False,
    "TRAIN_POUR"        :False,
    "TRAIN_FILL"        :False
    }

# abstract state class
class StateName():
    def __init__(self):
        self.stateName = "name of process"
        # change this to true if the state completes successfully
        self.success = False
        # tuples must be in (Event name, state class name) format
        self.transitionTable = []

    # do the business of running this state
    def run(self, context):
        print("[%s] Running" % self.stateName)


    def handler(self, eventDict, stateDict):
        # after completion, check events and transitions
        for transitionPair in self.transitionTable:
            transitionEvent = eventDict[transitionPair[0]]
            transitionTo = stateDict[transitionPair[1]]

            if transitionEvent:
                print("[%s] Transitioning to %s" % (self.stateName, transitionTo.stateName))
                return transitionTo
        
        return None

class Training(StateName):
    def __init__(self):
        self.stateName = "Training"
        self.transitionTable = [("IDLE", "Idle")] 

    def run(self, context):
        # Franka.reset_joints()
        # pose = RigidTransform(rotation=np.eye(3), translation=np.array([1, 1, 1]), from_frame='franka_tool', to_frame='world')
        # Franka.goto_pose(pose)
        Franka.run_guide_mode(10, block=True)
        print("[%s] Current pose:\n" % self.stateName, Franka.get_pose())
        print("[%s] Current joints:\n" % self.stateName, Franka.get_joints())

        while input("Continue? y/n") != "y":
            pass

class TrainGrip(StateName):
    def __init__(self):
        self.stateName = "TrainGrip"
        self.transitionTable = [("IDLE", "Idle")]

    def run(self, context):
        # Franka.open_gripper()
        Franka.close_gripper()
        # Franka.goto_gripper(width=0.045, grasp=True, force=5)
        # update the event in the context
        # context.eventDict["GRASPED_CUP"] = True

class Idle(StateName):
    def __init__(self):
        self.stateName = "Idle"
        self.transitionTable = [
            ("TRAIN", "Training"),
            ("TRAIN_GRIP", "TrainGrip"),
            ("SCALE_WATER_LOW", "MoveToFillPose"),
            # ("SCALE_WATER_LOW", "FillingCup"),
            # ("FILL_WATER_LOW", "FillingCup"),
            ("TRAIN_POUR", "MoveToScaleCup"),
            ("TRAIN_FILL", "MoveToFillPose")
            ] 

    
    def run(self, context):
        context.eventDict["GOAL_REACHED"] = False
        if context.mass_target < context.maxMass:
            context.eventDict["SCALE_WATER_LOW"] = True
            context.eventDict["SCALE_WATER_HIGH"] = False
        pass

        if context.eventDict["SCALE_WATER_HIGH"]:
            Franka.reset_joints()


class FillingCup(StateName):
    def __init__(self):
        self.stateName = "FillingCup"
        self.transitionTable = [("FILL_WATER_LOW", "MoveToScaleCup"),("IDLE", "Idle")]  
        self.hasPumped = False

    def run(self, context):
        context.eventDict["GOAL_REACHED"] = False
        # Franka.goto_joints(jointFillCup)
        
        pump = Bool()
        pump.data = True
        if not self.hasPumped:
            context.pumpPub.publish(pump)
            self.hasPumped = True
        if context.pump_is_done:
            context.pump_is_done = False
            self.hasPumped = False
            context.eventDict["FILL_WATER_LOW"] = True


class MoveToFillPose(StateName):
    def __init__(self):
        self.stateName = "MoveToFillPose"
        self.transitionTable = [("GOAL_REACHED", "FillingCup"),("IDLE", "Idle")]  

    def run(self, context):
        # Franka.goto_joints(jointFillCup)
        rrt(Franka, False, Franka.get_joints(),jointFillCup)
        context.eventDict["GOAL_REACHED"] = True



class MoveToScaleCup(StateName):
    def __init__(self):
        self.stateName = "MoveToScaleCup"
        self.transitionTable = [("GOAL_REACHED", "PourWater"),("IDLE", "Idle")]  

    def run(self, context):
        context.eventDict["FILL_WATER_LOW"] = False
        # Franka.goto_joints(jointPourCup)
        rrt(Franka, False, Franka.get_joints(),jointPourCup)
        context.eventDict["GOAL_REACHED"] = True



class PourWater(StateName):
    def __init__(self):
        self.stateName = "PourWater"
        self.transitionTable = [("SCALE_WATER_LOW", "MoveToFillPose"),("IDLE", "Idle"), ("SCALE_WATER_HIGH", "Idle")]

    def run(self, context):
        context.eventDict["GOAL_REACHED"] = False

        startPourPose = Franka.get_pose()

        rot69 = RigidTransform(
            rotation=RigidTransform.z_axis_rotation(np.deg2rad(69)),
            from_frame='franka_tool', to_frame='franka_tool'
        )
        rot26 = RigidTransform(
            rotation=RigidTransform.z_axis_rotation(np.deg2rad(26)),
            from_frame='franka_tool', to_frame='franka_tool'
        )
        rot20 = RigidTransform(
            rotation=RigidTransform.z_axis_rotation(np.deg2rad(20)),
            from_frame='franka_tool', to_frame='franka_tool'
        )

        h1 = 0.05
        h2 = 0.1
        pour69 = startPourPose * rot69
        pour95 = pour69 * rot26
        pour95.translation += [0,-0.02,h1] #move towards cup, up a little

        pour115_high = pour95 * rot20
        pour115_high.translation += [0,-0.05,h2] #close to cup, up more
        pour115_low = pour95 * rot20
        pour115_low.translation += [0,-0.05,-h1] #back down

        #Run through the sequence
        forceThresh1 = 3.75
        forceThresh2 = 2.75

        currForceTorque = Franka.get_ee_force_torque()
        Franka.goto_pose(pour69, duration=2, block=False)
        while currForceTorque[2] > forceThresh1 or not Franka.is_skill_done():
            currForceTorque = Franka.get_ee_force_torque()
        
        Franka.goto_pose(pour95, duration=1, block=False)
        while currForceTorque[2] > forceThresh2 or not Franka.is_skill_done():
            currForceTorque = Franka.get_ee_force_torque()
        
        Franka.goto_pose(pour115_high, duration=1)
        Franka.goto_pose(pour115_low, duration=1)
        
        # currForceTorque = Franka.get_ee_force_torque()


        if context.mass_target > context.maxMass:
            context.eventDict["SCALE_WATER_HIGH"] = True
            context.eventDict["SCALE_WATER_LOW"] = False



# list of all the states
stateList = [FillingCup, MoveToFillPose, MoveToScaleCup, PourWater, Training, Idle, TrainGrip]

