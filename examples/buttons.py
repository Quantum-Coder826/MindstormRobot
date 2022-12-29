#!/usr/bin/env python3

# this program will print in the terminal wich button was pressed on the brick.

from robot.brick import *

brick = mindstorms()

while True:
    key, isPressed = brick.getKey()

    if isPressed:
        endString = "was pressed"
    else:
        endString = "was released"
    
    if key == keys.Back:
        print("The Back key " + endString)
    elif key == keys.Center:
        print("The center key " + endString)
    elif key == keys.Down:
        print("The down key " + endString)
    elif key == keys.Left:
        print("The left key " + endString)
    elif key == keys.Right:
        print("The right key " + endString)
    elif key == keys.Up:
        print("The up key " + endString)
    