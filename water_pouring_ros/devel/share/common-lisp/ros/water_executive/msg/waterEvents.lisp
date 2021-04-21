; Auto-generated. Do not edit!


(cl:in-package water_executive-msg)


;//! \htmlinclude waterEvents.msg.html

(cl:defclass <waterEvents> (roslisp-msg-protocol:ros-message)
  ((Header
    :reader Header
    :initarg :Header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (CurState
    :reader CurState
    :initarg :CurState
    :type cl:string
    :initform "")
   (WATER_POURED
    :reader WATER_POURED
    :initarg :WATER_POURED
    :type cl:boolean
    :initform cl:nil)
   (GOAL_REACHED
    :reader GOAL_REACHED
    :initarg :GOAL_REACHED
    :type cl:boolean
    :initform cl:nil)
   (GRASPED_CUP
    :reader GRASPED_CUP
    :initarg :GRASPED_CUP
    :type cl:boolean
    :initform cl:nil)
   (WATER_LOW
    :reader WATER_LOW
    :initarg :WATER_LOW
    :type cl:boolean
    :initform cl:nil)
   (PUMPS_OFF
    :reader PUMPS_OFF
    :initarg :PUMPS_OFF
    :type cl:boolean
    :initform cl:nil)
   (UNGRASPED_CUP
    :reader UNGRASPED_CUP
    :initarg :UNGRASPED_CUP
    :type cl:boolean
    :initform cl:nil)
   (WATER_HIGH
    :reader WATER_HIGH
    :initarg :WATER_HIGH
    :type cl:boolean
    :initform cl:nil)
   (TEST_EVENT1
    :reader TEST_EVENT1
    :initarg :TEST_EVENT1
    :type cl:boolean
    :initform cl:nil)
   (TRAIN
    :reader TRAIN
    :initarg :TRAIN
    :type cl:boolean
    :initform cl:nil)
   (IDLE
    :reader IDLE
    :initarg :IDLE
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass waterEvents (<waterEvents>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <waterEvents>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'waterEvents)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name water_executive-msg:<waterEvents> is deprecated: use water_executive-msg:waterEvents instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:Header-val is deprecated.  Use water_executive-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'CurState-val :lambda-list '(m))
(cl:defmethod CurState-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:CurState-val is deprecated.  Use water_executive-msg:CurState instead.")
  (CurState m))

(cl:ensure-generic-function 'WATER_POURED-val :lambda-list '(m))
(cl:defmethod WATER_POURED-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:WATER_POURED-val is deprecated.  Use water_executive-msg:WATER_POURED instead.")
  (WATER_POURED m))

(cl:ensure-generic-function 'GOAL_REACHED-val :lambda-list '(m))
(cl:defmethod GOAL_REACHED-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:GOAL_REACHED-val is deprecated.  Use water_executive-msg:GOAL_REACHED instead.")
  (GOAL_REACHED m))

(cl:ensure-generic-function 'GRASPED_CUP-val :lambda-list '(m))
(cl:defmethod GRASPED_CUP-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:GRASPED_CUP-val is deprecated.  Use water_executive-msg:GRASPED_CUP instead.")
  (GRASPED_CUP m))

(cl:ensure-generic-function 'WATER_LOW-val :lambda-list '(m))
(cl:defmethod WATER_LOW-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:WATER_LOW-val is deprecated.  Use water_executive-msg:WATER_LOW instead.")
  (WATER_LOW m))

(cl:ensure-generic-function 'PUMPS_OFF-val :lambda-list '(m))
(cl:defmethod PUMPS_OFF-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:PUMPS_OFF-val is deprecated.  Use water_executive-msg:PUMPS_OFF instead.")
  (PUMPS_OFF m))

(cl:ensure-generic-function 'UNGRASPED_CUP-val :lambda-list '(m))
(cl:defmethod UNGRASPED_CUP-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:UNGRASPED_CUP-val is deprecated.  Use water_executive-msg:UNGRASPED_CUP instead.")
  (UNGRASPED_CUP m))

(cl:ensure-generic-function 'WATER_HIGH-val :lambda-list '(m))
(cl:defmethod WATER_HIGH-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:WATER_HIGH-val is deprecated.  Use water_executive-msg:WATER_HIGH instead.")
  (WATER_HIGH m))

(cl:ensure-generic-function 'TEST_EVENT1-val :lambda-list '(m))
(cl:defmethod TEST_EVENT1-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:TEST_EVENT1-val is deprecated.  Use water_executive-msg:TEST_EVENT1 instead.")
  (TEST_EVENT1 m))

(cl:ensure-generic-function 'TRAIN-val :lambda-list '(m))
(cl:defmethod TRAIN-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:TRAIN-val is deprecated.  Use water_executive-msg:TRAIN instead.")
  (TRAIN m))

(cl:ensure-generic-function 'IDLE-val :lambda-list '(m))
(cl:defmethod IDLE-val ((m <waterEvents>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader water_executive-msg:IDLE-val is deprecated.  Use water_executive-msg:IDLE instead.")
  (IDLE m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <waterEvents>) ostream)
  "Serializes a message object of type '<waterEvents>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'CurState))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'CurState))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'WATER_POURED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GOAL_REACHED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GRASPED_CUP) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'WATER_LOW) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'PUMPS_OFF) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'UNGRASPED_CUP) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'WATER_HIGH) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'TEST_EVENT1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'TRAIN) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'IDLE) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <waterEvents>) istream)
  "Deserializes a message object of type '<waterEvents>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'CurState) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'CurState) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'WATER_POURED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GOAL_REACHED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GRASPED_CUP) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'WATER_LOW) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'PUMPS_OFF) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'UNGRASPED_CUP) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'WATER_HIGH) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'TEST_EVENT1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'TRAIN) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'IDLE) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<waterEvents>)))
  "Returns string type for a message object of type '<waterEvents>"
  "water_executive/waterEvents")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'waterEvents)))
  "Returns string type for a message object of type 'waterEvents"
  "water_executive/waterEvents")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<waterEvents>)))
  "Returns md5sum for a message object of type '<waterEvents>"
  "58d63cb8190a1014155cdd0e074fe007")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'waterEvents)))
  "Returns md5sum for a message object of type 'waterEvents"
  "58d63cb8190a1014155cdd0e074fe007")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<waterEvents>)))
  "Returns full string definition for message of type '<waterEvents>"
  (cl:format cl:nil "Header Header ~%string CurState~%bool WATER_POURED ~%bool GOAL_REACHED~%bool GRASPED_CUP ~%bool WATER_LOW  ~%bool PUMPS_OFF   ~%bool UNGRASPED_CUP~%bool WATER_HIGH   ~%bool TEST_EVENT1  ~%bool TRAIN~%bool IDLE~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'waterEvents)))
  "Returns full string definition for message of type 'waterEvents"
  (cl:format cl:nil "Header Header ~%string CurState~%bool WATER_POURED ~%bool GOAL_REACHED~%bool GRASPED_CUP ~%bool WATER_LOW  ~%bool PUMPS_OFF   ~%bool UNGRASPED_CUP~%bool WATER_HIGH   ~%bool TEST_EVENT1  ~%bool TRAIN~%bool IDLE~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <waterEvents>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     4 (cl:length (cl:slot-value msg 'CurState))
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <waterEvents>))
  "Converts a ROS message object to a list"
  (cl:list 'waterEvents
    (cl:cons ':Header (Header msg))
    (cl:cons ':CurState (CurState msg))
    (cl:cons ':WATER_POURED (WATER_POURED msg))
    (cl:cons ':GOAL_REACHED (GOAL_REACHED msg))
    (cl:cons ':GRASPED_CUP (GRASPED_CUP msg))
    (cl:cons ':WATER_LOW (WATER_LOW msg))
    (cl:cons ':PUMPS_OFF (PUMPS_OFF msg))
    (cl:cons ':UNGRASPED_CUP (UNGRASPED_CUP msg))
    (cl:cons ':WATER_HIGH (WATER_HIGH msg))
    (cl:cons ':TEST_EVENT1 (TEST_EVENT1 msg))
    (cl:cons ':TRAIN (TRAIN msg))
    (cl:cons ':IDLE (IDLE msg))
))
