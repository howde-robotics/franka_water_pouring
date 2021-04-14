from autolab_core import RigidTransform
from frankapy import FrankaArm
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
    translation=np.array([0.47204678, -0.16422077,  0.37084254]),
    from_frame="franka_tool",
    to_frame="world"

)

targetPourWater = RigidTransform(
    rotation = np.array([[-0.02478788,  0.01748741,  0.99953976],
                         [ 0.03187658, -0.99931511,  0.01827435],
                         [ 0.99917476,  0.03231489,  0.02421393]]),
    translation=np.array([ 0.40814904, -0.06825581,  0.57436334]),
    from_frame='franka_tool',
    to_frame="world"
)

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
        Franka.reset_joints()
        # pose = RigidTransform(rotation=np.eye(3), translation=np.array([1, 1, 1]), from_frame='franka_tool', to_frame='world')
        # Franka.goto_pose(pose)
        Franka.run_guide_mode(10, block=True)
        print("[%s] Current pose:\n" % self.stateName, Franka.get_pose())

        while input("Continue? y/n") != "y":
            pass

class TrainGrip(StateName):
    def __init__(self):
        self.stateName = "TrainGrip"
        self.transitionTable = [("IDLE"), "Idle"]

    def run(self, context):
        Franka.goto_gripper(width=0.045, grasp=True, force=5)
        # update the event in the context
        context.eventDict["GRASPED_CUP"] = True

class Idle(StateName):
    def __init__(self):
        self.stateName = "Idle"
        self.transitionTable = [("TRAIN", "Training")] 

    
    def run(self, context):
        pass

class FillingCup(StateName):
    def __init__(self):
        self.stateName = "FillingCup"
        self.transitionTable = [("WATER_LOW", "StoppingPump")]  

    def run(self, context):
        Franka.goto_pose(targetFillCupGripper)




class StoppingPump(StateName):
    def __init__(self):
        self.stateName = "StoppingPump"
        self.transitionTable = [("PUMPS_OFF", "MoveToPourCup")]  



class MoveToPourCup(StateName):
    def __init__(self):
        self.stateName = "MoveToPourCup"
        self.transitionTable = [("WATER_LOW", "GraspCup"), ("WATER_HIGH", "UngraspCup")]  



class MoveToScaleCup(StateName):
    def __init__(self):
        self.stateName = "MoveToScaleCup"
        self.transitionTable = [("GOAL_REACHED", "PourWater")]  



class GraspCup(StateName):
    def __init__(self):
        self.stateName = "GraspCup"
        self.transitionTable = [
            ("GRASPED_CUP", "MoveToScaleCup"),
            ("IDLE", "Idle")
        ]

    def run(self, context):
        Franka.goto_gripper(width=0.045, grasp=True, force=5)
        # update the event in the context
        context.eventDict["GRASPED_CUP"] = True


class UngraspCup(StateName):
    def __init__(self):
        self.stateName = "UngraspCup"
        self.transitionTable = [("UNGRASPED_CUP", "MoveHome")]


class MoveHome(StateName):
    def __init__(self):
        self.stateName = "MoveHome"
        self.transitionTable = [("GOAL_REACHED", "FillingCup")]


class PourWater(StateName):
    def __init__(self):
        self.stateName = "PourWater"
        self.transitionTable = [("WATER_HIGH", "MoveToPourCup")]


# list of all the states
stateList = [FillingCup, StoppingPump, MoveToPourCup, MoveToScaleCup, GraspCup, UngraspCup, MoveHome, PourWater, Training, Idle]

eventDict = {
    "WATER_POURED"      :False,
    "GOAL_REACHED"      :False,
    "GRASPED_CUP"       :False,
    "WATER_LOW"         :False,
    "PUMPS_OFF"         :False,
    "UNGRASPED_CUP"     :False,
    "WATER_HIGH"        :False,
    "TEST_EVENT1"       :False,
    "TRAIN"             :False,
    "IDLE"              :False
    }