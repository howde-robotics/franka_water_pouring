// Generated by gencpp from file water_executive/waterEvents.msg
// DO NOT EDIT!


#ifndef WATER_EXECUTIVE_MESSAGE_WATEREVENTS_H
#define WATER_EXECUTIVE_MESSAGE_WATEREVENTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace water_executive
{
template <class ContainerAllocator>
struct waterEvents_
{
  typedef waterEvents_<ContainerAllocator> Type;

  waterEvents_()
    : Header()
    , CurState()
    , WATER_POURED(false)
    , GOAL_REACHED(false)
    , GRASPED_CUP(false)
    , WATER_LOW(false)
    , PUMPS_OFF(false)
    , UNGRASPED_CUP(false)
    , WATER_HIGH(false)
    , TEST_EVENT1(false)
    , TRAIN(false)
    , IDLE(false)  {
    }
  waterEvents_(const ContainerAllocator& _alloc)
    : Header(_alloc)
    , CurState(_alloc)
    , WATER_POURED(false)
    , GOAL_REACHED(false)
    , GRASPED_CUP(false)
    , WATER_LOW(false)
    , PUMPS_OFF(false)
    , UNGRASPED_CUP(false)
    , WATER_HIGH(false)
    , TEST_EVENT1(false)
    , TRAIN(false)
    , IDLE(false)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _Header_type;
  _Header_type Header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _CurState_type;
  _CurState_type CurState;

   typedef uint8_t _WATER_POURED_type;
  _WATER_POURED_type WATER_POURED;

   typedef uint8_t _GOAL_REACHED_type;
  _GOAL_REACHED_type GOAL_REACHED;

   typedef uint8_t _GRASPED_CUP_type;
  _GRASPED_CUP_type GRASPED_CUP;

   typedef uint8_t _WATER_LOW_type;
  _WATER_LOW_type WATER_LOW;

   typedef uint8_t _PUMPS_OFF_type;
  _PUMPS_OFF_type PUMPS_OFF;

   typedef uint8_t _UNGRASPED_CUP_type;
  _UNGRASPED_CUP_type UNGRASPED_CUP;

   typedef uint8_t _WATER_HIGH_type;
  _WATER_HIGH_type WATER_HIGH;

   typedef uint8_t _TEST_EVENT1_type;
  _TEST_EVENT1_type TEST_EVENT1;

   typedef uint8_t _TRAIN_type;
  _TRAIN_type TRAIN;

   typedef uint8_t _IDLE_type;
  _IDLE_type IDLE;





  typedef boost::shared_ptr< ::water_executive::waterEvents_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::water_executive::waterEvents_<ContainerAllocator> const> ConstPtr;

}; // struct waterEvents_

typedef ::water_executive::waterEvents_<std::allocator<void> > waterEvents;

typedef boost::shared_ptr< ::water_executive::waterEvents > waterEventsPtr;
typedef boost::shared_ptr< ::water_executive::waterEvents const> waterEventsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::water_executive::waterEvents_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::water_executive::waterEvents_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::water_executive::waterEvents_<ContainerAllocator1> & lhs, const ::water_executive::waterEvents_<ContainerAllocator2> & rhs)
{
  return lhs.Header == rhs.Header &&
    lhs.CurState == rhs.CurState &&
    lhs.WATER_POURED == rhs.WATER_POURED &&
    lhs.GOAL_REACHED == rhs.GOAL_REACHED &&
    lhs.GRASPED_CUP == rhs.GRASPED_CUP &&
    lhs.WATER_LOW == rhs.WATER_LOW &&
    lhs.PUMPS_OFF == rhs.PUMPS_OFF &&
    lhs.UNGRASPED_CUP == rhs.UNGRASPED_CUP &&
    lhs.WATER_HIGH == rhs.WATER_HIGH &&
    lhs.TEST_EVENT1 == rhs.TEST_EVENT1 &&
    lhs.TRAIN == rhs.TRAIN &&
    lhs.IDLE == rhs.IDLE;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::water_executive::waterEvents_<ContainerAllocator1> & lhs, const ::water_executive::waterEvents_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace water_executive

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::water_executive::waterEvents_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::water_executive::waterEvents_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::water_executive::waterEvents_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::water_executive::waterEvents_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::water_executive::waterEvents_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::water_executive::waterEvents_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::water_executive::waterEvents_<ContainerAllocator> >
{
  static const char* value()
  {
    return "58d63cb8190a1014155cdd0e074fe007";
  }

  static const char* value(const ::water_executive::waterEvents_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x58d63cb8190a1014ULL;
  static const uint64_t static_value2 = 0x155cdd0e074fe007ULL;
};

template<class ContainerAllocator>
struct DataType< ::water_executive::waterEvents_<ContainerAllocator> >
{
  static const char* value()
  {
    return "water_executive/waterEvents";
  }

  static const char* value(const ::water_executive::waterEvents_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::water_executive::waterEvents_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header Header \n"
"string CurState\n"
"bool WATER_POURED \n"
"bool GOAL_REACHED\n"
"bool GRASPED_CUP \n"
"bool WATER_LOW  \n"
"bool PUMPS_OFF   \n"
"bool UNGRASPED_CUP\n"
"bool WATER_HIGH   \n"
"bool TEST_EVENT1  \n"
"bool TRAIN\n"
"bool IDLE\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::water_executive::waterEvents_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::water_executive::waterEvents_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Header);
      stream.next(m.CurState);
      stream.next(m.WATER_POURED);
      stream.next(m.GOAL_REACHED);
      stream.next(m.GRASPED_CUP);
      stream.next(m.WATER_LOW);
      stream.next(m.PUMPS_OFF);
      stream.next(m.UNGRASPED_CUP);
      stream.next(m.WATER_HIGH);
      stream.next(m.TEST_EVENT1);
      stream.next(m.TRAIN);
      stream.next(m.IDLE);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct waterEvents_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::water_executive::waterEvents_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::water_executive::waterEvents_<ContainerAllocator>& v)
  {
    s << indent << "Header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.Header);
    s << indent << "CurState: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.CurState);
    s << indent << "WATER_POURED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.WATER_POURED);
    s << indent << "GOAL_REACHED: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GOAL_REACHED);
    s << indent << "GRASPED_CUP: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.GRASPED_CUP);
    s << indent << "WATER_LOW: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.WATER_LOW);
    s << indent << "PUMPS_OFF: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.PUMPS_OFF);
    s << indent << "UNGRASPED_CUP: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.UNGRASPED_CUP);
    s << indent << "WATER_HIGH: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.WATER_HIGH);
    s << indent << "TEST_EVENT1: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.TEST_EVENT1);
    s << indent << "TRAIN: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.TRAIN);
    s << indent << "IDLE: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.IDLE);
  }
};

} // namespace message_operations
} // namespace ros

#endif // WATER_EXECUTIVE_MESSAGE_WATEREVENTS_H
