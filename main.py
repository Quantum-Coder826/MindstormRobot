from robot.brick import *

from time import sleep

brick = mindstroms()
while True:
    brick.setLed(led.leftGreen, 0)
    brick.setLed(led.rightGreen, 0)
    sleep(1)
    brick.setLed(led.leftGreen, 255)
    brick.setLed(led.rightGreen, 255)
