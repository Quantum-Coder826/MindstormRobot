#!/usr/bin/env python3
# * python3 /home/robot/MindstormsRobot/main.py

from drivers.brick import *
from drivers.sensor import *
from drivers.motor import *

from os import listdir
from time import sleep
import sys

print("ready")

keys = [(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]

brick.configure()

IR = sensor(ports.in4)
IR.setMode("IR-REMOTE")

rightMotor = motor(ports.outA)
leftMotor = motor(ports.outD)
rightMotor.setStopAction("coast")
leftMotor.setStopAction("coast")

try:
    while True:
        key = IR.getValue()
        rightMotor.runCommand("run-direct", duty=keys[key][0])
        leftMotor.runCommand("run-direct", duty=keys[key][1])


except KeyboardInterrupt:
    print("exiting")
    brick.resetAll()
    sys.exit(0)