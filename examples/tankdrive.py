"""
Demo file to showcase tankdrive using de lego mindstorms education edition driving base,
IR sensor and IR remote
"""

from robot.brick import *
from robot.motor import *
from robot.sensor import *

brick.configure()

keymap = [(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]

leftmotor = motor(ports.outD)
rightmotor = motor(ports.outA)

IR = sensor(ports.in4)

IR.setMode("IR-REMOTE")

leftmotor.runDuty(0)
rightmotor.runDuty(0)

try:
    while True:
        key = IR.getValue() # no argument os channel 1 will be read

        leftmotor.setDuty(keymap[key][0])
        rightmotor.setDuty(keymap[key][0])
        
except KeyboardInterrupt: # exit program on control-C
    print(" exiting ")
    brick.resetAll()
    exit()