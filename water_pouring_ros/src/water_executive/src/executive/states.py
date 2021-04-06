class StateName():
    def __init__(self):
        self.stateName = "name of process"
        # change this to true if the state completes successfully
        self.success = False

    # do the business of running this state
    def run(self):
        pass

class FillingCup():
    def __init__(self):
        self.stateName = "Filling Cup"
        self.success = False


    def run(self):
            pass


class StoppingPump():
    def __init__(self):
        self.stateName = "Stopping Pump"
        self.success = False


    def run(self):
            pass

class MoveToPourCup():
    def __init__(self):
        self.stateName = "Move To Pour Cup"
        self.success = False


    def run(self):
            pass

class MoveToScaleCup():
    def __init__(self):
        self.stateName = "Move To Scale Cup"
        self.success = False


    def run(self):
            pass

class GraspCup():
    def __init__(self):
        self.stateName = "Grasp Cup"
        self.success = False


    def run(self):
            pass

class UngraspCup():
    def __init__(self):
        self.stateName = "Ungrasp Cup"
        self.success = False


    def run(self):
            pass

class MoveHome():
    def __init__(self):
        self.stateName = "Move Home"
        self.success = False

    def run(self):
        pass

class PourWater():
    def __init__(self):
        self.stateName = "Pour Water"
        self.success = False


    def run(self):
            pass

# list of all the states
stateList = [FillingCup, StoppingPump, MoveToPourCup, MoveToScaleCup, GraspCup, UngraspCup, MoveHome]