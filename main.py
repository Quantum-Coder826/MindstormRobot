from robot.brick import *
from robot.motor import *
from robot.sensor import *

brick = mindstorms()

button = sensor(ports.in1)

while True:
    if button.isPressed():
        brick.setLed(led.leftRed, 255)
