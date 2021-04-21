#! /usr/bin/env python
import serial
import time

portName = "/dev/ttyACM0"
serialPort = serial.Serial(port=portName, baudrate=9600)
 
counter = 32

while True:
    counter += 1
    # serialPort.write(counter)
    print(serialPort.readline())
    time.sleep(0.1)
    if counter == 255:
        counter = 32