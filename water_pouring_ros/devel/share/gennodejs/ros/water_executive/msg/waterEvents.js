// Auto-generated. Do not edit!

// (in-package water_executive.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class waterEvents {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Header = null;
      this.CurState = null;
      this.WATER_POURED = null;
      this.GOAL_REACHED = null;
      this.GRASPED_CUP = null;
      this.WATER_LOW = null;
      this.PUMPS_OFF = null;
      this.UNGRASPED_CUP = null;
      this.WATER_HIGH = null;
      this.TEST_EVENT1 = null;
      this.TRAIN = null;
      this.IDLE = null;
    }
    else {
      if (initObj.hasOwnProperty('Header')) {
        this.Header = initObj.Header
      }
      else {
        this.Header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('CurState')) {
        this.CurState = initObj.CurState
      }
      else {
        this.CurState = '';
      }
      if (initObj.hasOwnProperty('WATER_POURED')) {
        this.WATER_POURED = initObj.WATER_POURED
      }
      else {
        this.WATER_POURED = false;
      }
      if (initObj.hasOwnProperty('GOAL_REACHED')) {
        this.GOAL_REACHED = initObj.GOAL_REACHED
      }
      else {
        this.GOAL_REACHED = false;
      }
      if (initObj.hasOwnProperty('GRASPED_CUP')) {
        this.GRASPED_CUP = initObj.GRASPED_CUP
      }
      else {
        this.GRASPED_CUP = false;
      }
      if (initObj.hasOwnProperty('WATER_LOW')) {
        this.WATER_LOW = initObj.WATER_LOW
      }
      else {
        this.WATER_LOW = false;
      }
      if (initObj.hasOwnProperty('PUMPS_OFF')) {
        this.PUMPS_OFF = initObj.PUMPS_OFF
      }
      else {
        this.PUMPS_OFF = false;
      }
      if (initObj.hasOwnProperty('UNGRASPED_CUP')) {
        this.UNGRASPED_CUP = initObj.UNGRASPED_CUP
      }
      else {
        this.UNGRASPED_CUP = false;
      }
      if (initObj.hasOwnProperty('WATER_HIGH')) {
        this.WATER_HIGH = initObj.WATER_HIGH
      }
      else {
        this.WATER_HIGH = false;
      }
      if (initObj.hasOwnProperty('TEST_EVENT1')) {
        this.TEST_EVENT1 = initObj.TEST_EVENT1
      }
      else {
        this.TEST_EVENT1 = false;
      }
      if (initObj.hasOwnProperty('TRAIN')) {
        this.TRAIN = initObj.TRAIN
      }
      else {
        this.TRAIN = false;
      }
      if (initObj.hasOwnProperty('IDLE')) {
        this.IDLE = initObj.IDLE
      }
      else {
        this.IDLE = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type waterEvents
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [CurState]
    bufferOffset = _serializer.string(obj.CurState, buffer, bufferOffset);
    // Serialize message field [WATER_POURED]
    bufferOffset = _serializer.bool(obj.WATER_POURED, buffer, bufferOffset);
    // Serialize message field [GOAL_REACHED]
    bufferOffset = _serializer.bool(obj.GOAL_REACHED, buffer, bufferOffset);
    // Serialize message field [GRASPED_CUP]
    bufferOffset = _serializer.bool(obj.GRASPED_CUP, buffer, bufferOffset);
    // Serialize message field [WATER_LOW]
    bufferOffset = _serializer.bool(obj.WATER_LOW, buffer, bufferOffset);
    // Serialize message field [PUMPS_OFF]
    bufferOffset = _serializer.bool(obj.PUMPS_OFF, buffer, bufferOffset);
    // Serialize message field [UNGRASPED_CUP]
    bufferOffset = _serializer.bool(obj.UNGRASPED_CUP, buffer, bufferOffset);
    // Serialize message field [WATER_HIGH]
    bufferOffset = _serializer.bool(obj.WATER_HIGH, buffer, bufferOffset);
    // Serialize message field [TEST_EVENT1]
    bufferOffset = _serializer.bool(obj.TEST_EVENT1, buffer, bufferOffset);
    // Serialize message field [TRAIN]
    bufferOffset = _serializer.bool(obj.TRAIN, buffer, bufferOffset);
    // Serialize message field [IDLE]
    bufferOffset = _serializer.bool(obj.IDLE, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type waterEvents
    let len;
    let data = new waterEvents(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [CurState]
    data.CurState = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [WATER_POURED]
    data.WATER_POURED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GOAL_REACHED]
    data.GOAL_REACHED = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [GRASPED_CUP]
    data.GRASPED_CUP = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [WATER_LOW]
    data.WATER_LOW = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [PUMPS_OFF]
    data.PUMPS_OFF = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [UNGRASPED_CUP]
    data.UNGRASPED_CUP = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [WATER_HIGH]
    data.WATER_HIGH = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [TEST_EVENT1]
    data.TEST_EVENT1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [TRAIN]
    data.TRAIN = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [IDLE]
    data.IDLE = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += object.CurState.length;
    return length + 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'water_executive/waterEvents';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '58d63cb8190a1014155cdd0e074fe007';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header Header 
    string CurState
    bool WATER_POURED 
    bool GOAL_REACHED
    bool GRASPED_CUP 
    bool WATER_LOW  
    bool PUMPS_OFF   
    bool UNGRASPED_CUP
    bool WATER_HIGH   
    bool TEST_EVENT1  
    bool TRAIN
    bool IDLE
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new waterEvents(null);
    if (msg.Header !== undefined) {
      resolved.Header = std_msgs.msg.Header.Resolve(msg.Header)
    }
    else {
      resolved.Header = new std_msgs.msg.Header()
    }

    if (msg.CurState !== undefined) {
      resolved.CurState = msg.CurState;
    }
    else {
      resolved.CurState = ''
    }

    if (msg.WATER_POURED !== undefined) {
      resolved.WATER_POURED = msg.WATER_POURED;
    }
    else {
      resolved.WATER_POURED = false
    }

    if (msg.GOAL_REACHED !== undefined) {
      resolved.GOAL_REACHED = msg.GOAL_REACHED;
    }
    else {
      resolved.GOAL_REACHED = false
    }

    if (msg.GRASPED_CUP !== undefined) {
      resolved.GRASPED_CUP = msg.GRASPED_CUP;
    }
    else {
      resolved.GRASPED_CUP = false
    }

    if (msg.WATER_LOW !== undefined) {
      resolved.WATER_LOW = msg.WATER_LOW;
    }
    else {
      resolved.WATER_LOW = false
    }

    if (msg.PUMPS_OFF !== undefined) {
      resolved.PUMPS_OFF = msg.PUMPS_OFF;
    }
    else {
      resolved.PUMPS_OFF = false
    }

    if (msg.UNGRASPED_CUP !== undefined) {
      resolved.UNGRASPED_CUP = msg.UNGRASPED_CUP;
    }
    else {
      resolved.UNGRASPED_CUP = false
    }

    if (msg.WATER_HIGH !== undefined) {
      resolved.WATER_HIGH = msg.WATER_HIGH;
    }
    else {
      resolved.WATER_HIGH = false
    }

    if (msg.TEST_EVENT1 !== undefined) {
      resolved.TEST_EVENT1 = msg.TEST_EVENT1;
    }
    else {
      resolved.TEST_EVENT1 = false
    }

    if (msg.TRAIN !== undefined) {
      resolved.TRAIN = msg.TRAIN;
    }
    else {
      resolved.TRAIN = false
    }

    if (msg.IDLE !== undefined) {
      resolved.IDLE = msg.IDLE;
    }
    else {
      resolved.IDLE = false
    }

    return resolved;
    }
};

module.exports = waterEvents;
