#!/usr/bin/env python3
# * python3 /home/robot/MindstormsRobot/main.py

from drivers.brick import *
from drivers.motor import motor
from drivers.sensor import *

from os import listdir
from time import sleep
import sys

brick.configure()

motor = motor("A")
motor.setStopAction()
try:
    while True:
        motor.runCommand("run-to-rel-pos", speed=200, angle=90)
        sleep(1)
except KeyboardInterrupt:
    print("exiting")
    brick.resetAll()
    sys.exit(0)