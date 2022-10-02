from robot.brick import *
from robot.motor import *
from robot.sensor import *

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
    print(type(key))
    print(key)
    leftMotor.setDuty(keyMap[key][0])
    rightMotor.setDuty(keyMap[key][1])
