#!/usr/bin/env python3
# * python3 /home/robot/MindstormsRobot/main.py

from drivers.brick import *
from drivers.sensor import *

from os import listdir
from time import sleep
import sys

brick.configure()

US = sensor(port.in4)
US.setMode("US-DIST-CM")

try:
    while True:
        print(str(US.getValue()) + " CM")
except KeyboardInterrupt:
    print("exiting")
    brick.resetAll()
    sys.exit(0)