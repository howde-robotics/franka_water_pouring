#include "HX711.h"
#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Bool.h>

HX711 scaleTarget;
HX711 scaleFill;
ros::NodeHandle nh;

const uint8_t scaleFillDataPin = 4;
const uint8_t scaleFillClockPin = 5;
const uint8_t scaleTargetDataPin = 6;
const uint8_t scaleTargetClockPin = 7;
const uint8_t pumpToCupPin = 9;
const uint8_t pumpToFillPin = 8;

unsigned long StartTime;
unsigned long EndTime;

std_msgs::Float32 massTargetData;
std_msgs::Float32 massFillData;
std_msgs::Bool pumpIsDoneData;
bool pumpCupCmd = false;
bool pumpFillCmd = false;

float scaleTarget_data = 0;
float scaleFill_data = 0;

enum kState{
  pumpToFillCup,
  pumpToFrankaCup,
  idle
};

const float emaAlpha = 2.0/(1 + 20);//exponential moving average weighting term

kState state = idle;

ros::Publisher massTargetDataPub("mass_target", &massTargetData);
ros::Publisher massFillDataPub("mass_fill", &massFillData);
ros::Publisher pumpIsDonePub("pump_is_done", &pumpIsDoneData);

void togglePumpCup(const std_msgs::Bool& msg) {

  if (msg.data)
  {
    state = pumpToFillCup;
  } else 
  {
    state = idle;
  }
}
ros::Subscriber<std_msgs::Bool> togglePumpCupSub("/toggle_pump_to_cup", &togglePumpCup);

void setup()
{
  scaleTarget.begin(scaleTargetDataPin, scaleTargetClockPin);
  scaleFill.begin(scaleFillDataPin, scaleFillClockPin);

  pinMode(pumpToCupPin, OUTPUT);
  digitalWrite(pumpToCupPin, HIGH);

  pinMode(pumpToFillPin, OUTPUT);
  digitalWrite(pumpToFillPin, HIGH);

  pumpIsDoneData.data = true;

  nh.initNode();
  nh.advertise(massTargetDataPub);
  nh.advertise(massFillDataPub);
  nh.advertise(pumpIsDonePub);
  nh.subscribe(togglePumpCupSub);
  delay(3000);
}

void loop()
{
  float temp = scaleTarget.get_units(1);
  if (temp > 50000 && temp < 600000)
  {
    scaleTarget_data = (emaAlpha * temp) + (1.0 - emaAlpha) * scaleTarget_data;
    massTargetData.data = scaleTarget_data;
    massTargetDataPub.publish(&massTargetData);
  }

  temp = scaleFill.get_units(1);
  if (temp > 50000 && temp < 300000)
  {
    scaleFill_data = (emaAlpha * temp) + (1.0 - emaAlpha) * scaleFill_data;
    massFillData.data = scaleFill_data;
    massFillDataPub.publish(&massFillData);
  }


  if (state == pumpToFillCup)
  {
    if (scaleFill_data < 200000)
    {
      pumpFillCmd = true;
    } else
    {
      pumpFillCmd = false;
      state = pumpToFrankaCup;
    }
  } else if (state == pumpToFrankaCup)
  {
    if (scaleFill_data > 100000)
    {
      pumpCupCmd = true;
    } else
    {
      pumpCupCmd = false;
      state = idle;
      pumpIsDonePub.publish(&pumpIsDoneData);
    }
  }
 
  digitalWrite(pumpToCupPin, !pumpCupCmd);
  digitalWrite(pumpToFillPin, !pumpFillCmd);

  nh.spinOnce();
}
