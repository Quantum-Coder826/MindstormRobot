from robot.brick import *
from robot.sensor import *

map = [(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]

brick = mindstorms()

button = sensor(ports.in1)

while True:
    if button.isPressed():
        break
    else:
        brick.setLed(0,0)

brick.setLed(1,255)