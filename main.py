#!/usr/bin/env python3
# * python3 /home/robot/MindstormsRobot/main.py

from drivers import *
from os import listdir
import sys

brick.configure() # config the brick

try:
    while True:
        print(devices)
except KeyboardInterrupt:
    print("exiting")
    sys.exit(0)