#!/usr/bin/env python3
from os import listdir
import atexit

motorpath = "/sys/class/tacho-motor"
sensorpath = "/sys/class/lego-sensor"
ledpath = ["/sys/class/leds/led0:green:brick-status", "/sys/class/leds/led0:red:brick-status", "/sys/class/leds/led1:green:brick-status", "/sys/class/leds/led1:red:brick-status"]

# general functions
def readFile(path):
    f = open(str(path), "r")
    data = f.read()
    f.close()
    data = data.strip()  
    return str(data)

def writeFile(path, data):
    f = open(path, "w")
    f.write(str(data))
    f.close()

def exit_handler():
    print("exiting")
    mindstorms.reset()

class mindstorms:
    def __init__(lego_brick):
        mindstorms.reset()
        print("running")

    @staticmethod
    def reset(lego_brick):
        for i in range(0,3): # reset all leds
            if i == 0 or i == 2:
                writeFile(ledpath[i] + "/brightness", 255)
            else:
                writeFile(ledpath[i] + "/brightness", 0)
        for dir in listdir("/sys/class/tacho-motor"): # reset all motors
            writeFile("/sys/class/tacho-motor/" + str(dir) + "/command", "reset")

    def setLed(lego_brick, target = 0, value = 255): # changes the brightness of a led
        writeFile(ledpath[target] + "/brightness", value)

    # todo: figure out how the hell to read the buttons (https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ev3.html#buttons)
class ports:
    # all the ports
    outA = "ev3-ports:outA"
    outB = "ev3-ports:outB"
    outC = "ev3-ports:outC"
    outD = "ev3-ports:outD"

    in1 = "ev3-ports:in1"
    in2 = "ev3-ports:in2"
    in3 = "ev3-ports:in3"
    in4 = "ev3-ports:in4"

class led:
    # led codes
    leftGreen = 0
    leftRed = 1
    rightGreen = 2
    rightRed = 3

atexit.register(exit_handler)
