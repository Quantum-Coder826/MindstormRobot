from robot.brick import *
from robot.motor import *
from robot.sensor import *

brick = mindstroms()

leftMotor = motor(ports.outA)
rightMotor = motor(ports.outD)

sonar = sensor(ports.in4)

leftMotor.runDuty()
rightMotor.runDuty()

sonar.setMode("US-DIST-CM")

rightMotor.setDuty(50)
rightMotor.setDuty(50)

try:
    while True:
        if sonar.getValue() <= 7.0:
            leftMotor.setDuty(-50)
        rightMotor.setDuty(50)
except KeyboardInterrupt:
    print(" exiting ")
    brick.resetAll()
    exit()
