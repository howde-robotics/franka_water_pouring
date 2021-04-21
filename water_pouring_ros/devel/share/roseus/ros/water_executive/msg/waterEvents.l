;; Auto-generated. Do not edit!


(when (boundp 'water_executive::waterEvents)
  (if (not (find-package "WATER_EXECUTIVE"))
    (make-package "WATER_EXECUTIVE"))
  (shadow 'waterEvents (find-package "WATER_EXECUTIVE")))
(unless (find-package "WATER_EXECUTIVE::WATEREVENTS")
  (make-package "WATER_EXECUTIVE::WATEREVENTS"))

(in-package "ROS")
;;//! \htmlinclude waterEvents.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass water_executive::waterEvents
  :super ros::object
  :slots (_Header _CurState _WATER_POURED _GOAL_REACHED _GRASPED_CUP _WATER_LOW _PUMPS_OFF _UNGRASPED_CUP _WATER_HIGH _TEST_EVENT1 _TRAIN _IDLE ))

(defmethod water_executive::waterEvents
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:CurState __CurState) "")
    ((:WATER_POURED __WATER_POURED) nil)
    ((:GOAL_REACHED __GOAL_REACHED) nil)
    ((:GRASPED_CUP __GRASPED_CUP) nil)
    ((:WATER_LOW __WATER_LOW) nil)
    ((:PUMPS_OFF __PUMPS_OFF) nil)
    ((:UNGRASPED_CUP __UNGRASPED_CUP) nil)
    ((:WATER_HIGH __WATER_HIGH) nil)
    ((:TEST_EVENT1 __TEST_EVENT1) nil)
    ((:TRAIN __TRAIN) nil)
    ((:IDLE __IDLE) nil)
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _CurState (string __CurState))
   (setq _WATER_POURED __WATER_POURED)
   (setq _GOAL_REACHED __GOAL_REACHED)
   (setq _GRASPED_CUP __GRASPED_CUP)
   (setq _WATER_LOW __WATER_LOW)
   (setq _PUMPS_OFF __PUMPS_OFF)
   (setq _UNGRASPED_CUP __UNGRASPED_CUP)
   (setq _WATER_HIGH __WATER_HIGH)
   (setq _TEST_EVENT1 __TEST_EVENT1)
   (setq _TRAIN __TRAIN)
   (setq _IDLE __IDLE)
   self)
  (:Header
   (&rest __Header)
   (if (keywordp (car __Header))
       (send* _Header __Header)
     (progn
       (if __Header (setq _Header (car __Header)))
       _Header)))
  (:CurState
   (&optional __CurState)
   (if __CurState (setq _CurState __CurState)) _CurState)
  (:WATER_POURED
   (&optional __WATER_POURED)
   (if __WATER_POURED (setq _WATER_POURED __WATER_POURED)) _WATER_POURED)
  (:GOAL_REACHED
   (&optional __GOAL_REACHED)
   (if __GOAL_REACHED (setq _GOAL_REACHED __GOAL_REACHED)) _GOAL_REACHED)
  (:GRASPED_CUP
   (&optional __GRASPED_CUP)
   (if __GRASPED_CUP (setq _GRASPED_CUP __GRASPED_CUP)) _GRASPED_CUP)
  (:WATER_LOW
   (&optional __WATER_LOW)
   (if __WATER_LOW (setq _WATER_LOW __WATER_LOW)) _WATER_LOW)
  (:PUMPS_OFF
   (&optional __PUMPS_OFF)
   (if __PUMPS_OFF (setq _PUMPS_OFF __PUMPS_OFF)) _PUMPS_OFF)
  (:UNGRASPED_CUP
   (&optional __UNGRASPED_CUP)
   (if __UNGRASPED_CUP (setq _UNGRASPED_CUP __UNGRASPED_CUP)) _UNGRASPED_CUP)
  (:WATER_HIGH
   (&optional __WATER_HIGH)
   (if __WATER_HIGH (setq _WATER_HIGH __WATER_HIGH)) _WATER_HIGH)
  (:TEST_EVENT1
   (&optional __TEST_EVENT1)
   (if __TEST_EVENT1 (setq _TEST_EVENT1 __TEST_EVENT1)) _TEST_EVENT1)
  (:TRAIN
   (&optional __TRAIN)
   (if __TRAIN (setq _TRAIN __TRAIN)) _TRAIN)
  (:IDLE
   (&optional __IDLE)
   (if __IDLE (setq _IDLE __IDLE)) _IDLE)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; string _CurState
    4 (length _CurState)
    ;; bool _WATER_POURED
    1
    ;; bool _GOAL_REACHED
    1
    ;; bool _GRASPED_CUP
    1
    ;; bool _WATER_LOW
    1
    ;; bool _PUMPS_OFF
    1
    ;; bool _UNGRASPED_CUP
    1
    ;; bool _WATER_HIGH
    1
    ;; bool _TEST_EVENT1
    1
    ;; bool _TRAIN
    1
    ;; bool _IDLE
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; string _CurState
       (write-long (length _CurState) s) (princ _CurState s)
     ;; bool _WATER_POURED
       (if _WATER_POURED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GOAL_REACHED
       (if _GOAL_REACHED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GRASPED_CUP
       (if _GRASPED_CUP (write-byte -1 s) (write-byte 0 s))
     ;; bool _WATER_LOW
       (if _WATER_LOW (write-byte -1 s) (write-byte 0 s))
     ;; bool _PUMPS_OFF
       (if _PUMPS_OFF (write-byte -1 s) (write-byte 0 s))
     ;; bool _UNGRASPED_CUP
       (if _UNGRASPED_CUP (write-byte -1 s) (write-byte 0 s))
     ;; bool _WATER_HIGH
       (if _WATER_HIGH (write-byte -1 s) (write-byte 0 s))
     ;; bool _TEST_EVENT1
       (if _TEST_EVENT1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _TRAIN
       (if _TRAIN (write-byte -1 s) (write-byte 0 s))
     ;; bool _IDLE
       (if _IDLE (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _Header
     (send _Header :deserialize buf ptr-) (incf ptr- (send _Header :serialization-length))
   ;; string _CurState
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _CurState (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _WATER_POURED
     (setq _WATER_POURED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GOAL_REACHED
     (setq _GOAL_REACHED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GRASPED_CUP
     (setq _GRASPED_CUP (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _WATER_LOW
     (setq _WATER_LOW (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _PUMPS_OFF
     (setq _PUMPS_OFF (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _UNGRASPED_CUP
     (setq _UNGRASPED_CUP (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _WATER_HIGH
     (setq _WATER_HIGH (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _TEST_EVENT1
     (setq _TEST_EVENT1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _TRAIN
     (setq _TRAIN (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _IDLE
     (setq _IDLE (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get water_executive::waterEvents :md5sum-) "58d63cb8190a1014155cdd0e074fe007")
(setf (get water_executive::waterEvents :datatype-) "water_executive/waterEvents")
(setf (get water_executive::waterEvents :definition-)
      "Header Header 
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

")



(provide :water_executive/waterEvents "58d63cb8190a1014155cdd0e074fe007")


