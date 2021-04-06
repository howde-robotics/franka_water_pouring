#! /usr/bin/env python
import rospy
import numpy as np 
import abc
import states

class StateName():
    def __init__(self):
        self.stateName = "name of process"
        # change this to true if the state completes successfully
        self.success = False

    # do the business of running this state
    def run(self):
        pass


class WaterExecutive():
    def __init__(self, stateDict):
        self.stateDict = stateDict
        self.state = "Initializing"

    def stateMachine(self):
        pass



if __name__ == "__main__":
    stateList = states.stateList