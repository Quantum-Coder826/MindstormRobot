from robot.brick import *
from robot.motor import *
from robot.sensor import *
import signal

keyMap = [(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]

brick = mindstorms()

leftMotor = motor(ports.outB)
rightMotor = motor(ports.outC)
leftMotor.sendCommand("run-direct")
rightMotor.sendCommand("run-direct")

IR = sensor(ports.in4)
IR.setMode("IR-REMOTE")

while True:
    key = IR.getValue()
    if key == 10:
        brick.setLed(1,255)
        brick.setLed(3,255)
    elif key == 11:
        brick.setLed(0,0)
        brick.setLed(2,0)
        brick.setLed(1,255)
        brick.setLed(3,255)
    else:
        brick.resetLed()
    leftMotor.setDuty(keyMap[key][0])
    rightMotor.setDuty(keyMap[key][1])
