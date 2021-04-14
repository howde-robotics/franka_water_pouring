#! /usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from water_executive.msg import events


class EventManager():
    def __init__(self):
        _eventPub = rospy.Publisher("/water_pouring/events", String, queue_size=1)
        self.timerFreq = 20

        while not rospy.is_shutdown():
            rospy.sleep(1.0/self.timerFreq)

if __name__ == "__main__":
    rospy.init_node("event_manager")
    try:
        executive = EventManager()
    except rospy.ROSInitException:
        pass