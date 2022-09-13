from robot.brick import *
from robot.motor import *
from robot.sensor import *
# test comment/comit
print("running")

map = [(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]

brick = mindstroms()

rightMotor = motor(ports.outD)
leftMotor = motor(ports.outA)
IR = sensor(ports.in4)

rightMotor.runDuty(0)
leftMotor.runDuty(0)
IR.setMode("IR-REMOTE")

try:
    while True:
        key = IR.getValue()
        rightMotor.setDuty(map[key][0])
        leftMotor.setDuty(map[key][1])

except KeyboardInterrupt:
    print("exiting")
    brick.resetAll()
    exit()
