#!/usr/bin/env python3
# * python3 /home/robot/MindstormsRobot/main.py

from drivers import *
from os import listdir
import sys

brick.configure()

motor = motor("A")
print(devices)

try:
    motor.runCommand("run-to-abs-pos", speed=200, angle=90)
except KeyboardInterrupt:
    print("exiting")
    brick.resetAll()
    sys.exit(0)