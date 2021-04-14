#! /usr/bin/env python
import rospy
import numpy as np 
import abc
from std_msgs.msg import String
import states


class WaterExecutive():
    def __init__(self, entryState):
        # states for the system
        self.stateDict = {}

        # populate state dictionary
        for state in states.stateList:
            temp = state()
            self.stateDict[temp.stateName] = temp

        self.state = self.stateDict[entryState]

        # events for the system
        self.eventDict = states.eventDict

        print("[EXEC] Resetting Robot")
        states.Franka.reset_joints()

        # run the node
        self.rosInterface()

        while not rospy.is_shutdown():
            self.stateMachine()
            rospy.sleep(1.0/self.timerFreq)

    def stateMachine(self):
        print("[EXEC] Run State: %s" % self.state.stateName, end="\r")
        self.state.run(self)
        newState = self.state.handler(self.eventDict, self.stateDict)

        # handle the transition
        if newState is not None:
            self.state = newState


    # gather events
    def eventCallback(self, msg):
        event = msg.data
        print("\n[EXEC] Event Registered: %s" % event)
        self.resetEvents(target=event)

    # reset events to false, if passed an arg will toggle event
    def resetEvents(self, target=None):
        if target is None:
            for key in self.eventDict:
                self.eventDict[key] = False
            print("[EVENTS] Reset events to false")

        else:
            self.eventDict[target] = not self.eventDict[target]
            print("[EVENTS] %s changed to %r" % (target, self.eventDict[target]))

    # all the ros stuff
    def rosInterface(self):
        self.timerFreq = float(rospy.get_param("~exec_spin_rate", '20'))
        self.subEvents = rospy.Subscriber("/water_pouring/events", String, queue_size=1, callback=self.eventCallback)


if __name__ == "__main__":
    # rospy.init_node("water_executive")
    try:
        executive = WaterExecutive("Idle")
    except rospy.ROSInitException:
        pass
