from autolab_core import RigidTransform
from frankapy import FrankaArm
from std_msgs.msg import Bool
import time
import numpy as np

# main franka object
print("[STATES] Starting Robot")
Franka = FrankaArm()

# targets with GRIPPER
targetResCupGripper = RigidTransform(
    rotation = np.array([[ 0.99859754,  0.00794212,  0.05216007],
                         [ 0.00697227, -0.99979027,  0.01874966],
                         [ 0.05229804, -0.01835969, -0.99846271]]),
    translation = np.array([0.42077702, 0.31785366, 0.38082516]),
    from_frame="franka_tool",
    to_frame="world"
    )

targetFillCupGripper = RigidTransform(
    rotation = np.array([[ 0.99991559, -0.0016129 ,  0.01212235],
                         [-0.00173914, -0.99993467,  0.01041035],
                         [ 0.01210476, -0.01043055, -0.99987233]]),
    translation = np.array([0.547199, 0.03331735, 0.20330742]),
    from_frame="franka_tool",
    to_frame="world"
    )

targetPourCupGripper = RigidTransform(
    rotation = np.array([[ 0.99875038, -0.04795637,  0.01336468],
                         [-0.04786111, -0.99881725, -0.00735915],
                         [ 0.01370179,  0.0067103,  -0.99988361]]),
    translation=np.array([ 0.38429699, -0.28107915,  0.56759486]),
    from_frame="franka_tool",
    to_frame="world"

)

jointFillCup =  np.array([-0.00523853, -0.02406041,  0.00771755, -2.39707949, -0.0693488,   3.73495897,  0.78488679])
jointPourCup = np.array([ 0.59937575, -0.70281775, -1.05938841, -2.45454394, -0.72683186,  3.53392083, 0.78463731])
jointPour = np.array([ 0.59937575, -0.70281775, -1.05938841, -2.45454394, -0.72683186,  3.53392083, np.pi/1.2])

targetPourWater = RigidTransform(
    rotation = np.array([[-0.03620562, -0.00390866,  0.99933672],
                         [-0.7004525,  -0.71314301, -0.02816644],
                         [ 0.71278008, -0.70100769,  0.02308195]]),
    translation=np.array([ 0.40814904, -0.06825581,  0.57436334]),
    from_frame='franka_tool',
    to_frame="world"
)

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
            ("SCALE_WATER_LOW", "FillingCup"),
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
        Franka.goto_joints(jointFillCup)
        
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
        self.transitionTable = [("GOAL_REACHED", "Idle"),("IDLE", "Idle")]  

    def run(self, context):
        Franka.goto_joints(jointFillCup)
        context.eventDict["GOAL_REACHED"] = True



class MoveToScaleCup(StateName):
    def __init__(self):
        self.stateName = "MoveToScaleCup"
        self.transitionTable = [("GOAL_REACHED", "PourWater"),("IDLE", "Idle")]  

    def run(self, context):
        context.eventDict["FILL_WATER_LOW"] = False
        Franka.goto_joints(jointPourCup)
        context.eventDict["GOAL_REACHED"] = True



class PourWater(StateName):
    def __init__(self):
        self.stateName = "PourWater"
        self.transitionTable = [("SCALE_WATER_LOW", "MoveToFillPose"),("IDLE", "Idle"), ("SCALE_WATER_HIGH", "Idle")]

    def run(self, context):
        context.eventDict["GOAL_REACHED"] = False
        Franka.goto_joints(jointPour)

        if context.mass_target > context.maxMass:
            context.eventDict["SCALE_WATER_HIGH"] = True
            context.eventDict["SCALE_WATER_LOW"] = False



# list of all the states
stateList = [FillingCup, MoveToFillPose, MoveToScaleCup, PourWater, Training, Idle, TrainGrip]

