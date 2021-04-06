import abc
class StateName(abc.ABC):
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

class FillingCup(StateName):
    def __init__(self):
        self.stateName = "FillingCup"
        self.transitionTable = [("WATER_LOW", "StoppingPump")]  


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
        self.transitionTable = [("GRASPED_CUP", "MoveToScaleCup")]


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
stateList = [FillingCup, StoppingPump, MoveToPourCup, MoveToScaleCup, GraspCup, UngraspCup, MoveHome, PourWater]