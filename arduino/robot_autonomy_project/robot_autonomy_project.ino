#include "HX711.h"
#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Bool.h>

HX711 scale;
ros::NodeHandle nh;

const uint8_t scaleDataPin = 6;
const uint8_t scaleClockPin = 7;
const uint8_t pumpToCupPin = 8;
const uint8_t pumpToReservoirPin = 9;

unsigned long StartTime;
unsigned long EndTime;

std_msgs::Float32 massData;
bool pumpCmd = false;

ros::Publisher massDataPub("mass_data", &massData);

void togglePumpCup(const std_msgs::Bool& msg) {

  bool state = msg.data;
  if (state == true)
  {
    pumpCmd = true;
  } else 
  {
    pumpCmd = false;
  }
}
ros::Subscriber<std_msgs::Bool> togglePumpCupSub("/toggle_pump_to_cup", &togglePumpCup);

void setup()
{
  scale.begin(scaleDataPin, scaleClockPin);

  pinMode(pumpToCupPin, OUTPUT);
  digitalWrite(pumpToCupPin, HIGH);

  nh.initNode();
  nh.advertise(massDataPub);
  nh.subscribe(togglePumpCupSub);
}

void loop()
{
  float scale_data = scale.get_units(1);
  massData.data = scale_data;
  massDataPub.publish(&massData);

  if (scale_data > 100000)
  {
    pumpCmd = false;
  }
  
  digitalWrite(pumpToCupPin, !pumpCmd);

  nh.spinOnce();
}
