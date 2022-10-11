from robot.brick import *
from robot.motor import *
from robot.sensor import *

brick = mindstorms()

leftMotor = motor(ports.outB)
rightMotor = motor(ports.outC)
leftMotor.sendCommand("run-direct")
rightMotor.sendCommand("run-direct")

sonar = sensor(ports.in4)
sonar.setMode("US-DIST-CM")

while True:
    if sonar.getValue() <= 13:
        leftMotor.setDuty(0)
    else:
        leftMotor.setDuty(50)