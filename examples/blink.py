#!/usr/bin/env python3

# this script is a simple blink script
# the script will blink both leds on the brick green every second

from robot.brick import *
from time import sleep

brick = mindstorms()

brick.clearLeds()   # trun off all leds

while True:
    brick.setLed(led.leftGreen, 255)    # trun on the leds
    brick.setLed(led.rightGreen, 255)
    sleep(1)                            # wait 1 second
    brick.clearLeds()