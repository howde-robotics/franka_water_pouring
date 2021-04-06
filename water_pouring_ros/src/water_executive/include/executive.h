#include <ros/ros.h>
#include <vector>


class Executive {

    std::vector<int> systemState;

    // possible events 
    enum EventCodes {
        SCALE_EMPTY,
        SCALE_FULL,
        PUMPS_EMPTY,
        PUMPS_READY
    };

    // event property for states to poll
    EventCodes event;

    enum StateCodes {
        POUR_WATER,
        FILLUP_CUP,
        MOVE_TO_POUR,
        MOVE_TO_FILL,
        GRASP_CUP,
        UNGRASP_CUP,
        MOVE_HOME
    };

    StateCodes stateName;

};


class AbstractState {
    // name of state
    std::string stateName;
    // where everything happens
    virtual void run() = 0;
};