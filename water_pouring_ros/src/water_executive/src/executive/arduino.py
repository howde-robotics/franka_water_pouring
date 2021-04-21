#! /usr/bin/env python
import serial
import time

portName = "/dev/tty"
serialPort = serial.serialcli.Serial(portName)
counter = 32

while True:
    counter += 1
    serialPort.write(counter)
    print(serialPort.readline())
    time.sleep(0.1)
    if counter == 255:
        counter = 32