#!/usr/bin/env python3

# In this program you can use the brick buttons to contorl a tacho motor.
# the motor must be connected to the A port
# a note when the maximum of minimum duty cyle is passed the program will chrash

from robot.brick import *
from robot.motor import *

brick = mindstorms()

motorSpeed = 0

myMotor = motor(ports.outA)
myMotor.sendCommand("run-direct")

while True:
    key, isPressed = brick.getKey()

    if key == keys.Up and isPressed:
        motorSpeed += 5
    elif key == keys.Down and isPressed:
        motorSpeed -= 5
    elif key == keys.Back and isPressed:
        motorSpeed = 0
    elif not isPressed:
        continue

    myMotor.setDuty(motorSpeed)
    print("The duty is: " + str(motorSpeed))
