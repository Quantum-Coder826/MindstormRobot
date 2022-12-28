#!/usr/bin/env python3
from os import listdir
import atexit
import signal

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
    writeFile(ledpath[0] + "/brightness", "255")
    writeFile(ledpath[1] + "/brightness", "0")
    writeFile(ledpath[2] + "/brightness", "255")
    writeFile(ledpath[3] + "/brightness", "0")

    for dir in listdir("/sys/class/tacho-motor"): # reset all motors
        writeFile("/sys/class/tacho-motor/" + str(dir) + "/command", "reset")

class mindstorms:
    def __init__(lego_brick):
        writeFile(ledpath[0] + "/brightness", "255")
        writeFile(ledpath[1] + "/brightness", "0")
        writeFile(ledpath[2] + "/brightness", "255")
        writeFile(ledpath[3] + "/brightness", "0")
        print("running")
    
    def setLed(lego_brick, target = 0, value = 255): # changes the brightness of a led
        writeFile(ledpath[target] + "/brightness", value)

    def clearLeds(lego_brick): # turns off all leds
        for i in range(0,3):
            writeFile(ledpath[i] + "/brightness", "0")

    def resetLeds(lego_brick): # set the leds on the brick to default state
        writeFile(ledpath[0] + "/brightness", "255")
        writeFile(ledpath[1] + "/brightness", "0")
        writeFile(ledpath[2] + "/brightness", "255")
        writeFile(ledpath[3] + "/brightness", "0")
        
    # get the key pressed on the brick
    def getKey(lego_brick):
        buttons = open("/dev/input/event1", "rb")

        buffer = buttons.read(32).hex()
        key = int(buffer[20:22], base=16)
        if int(buffer[25:26], base=16) == 1:
            keyDown = True
        if int(buffer[25:26], base=16) == 0:
            keyDown = False
        
        buttons.close()
        return key, keyDown
        



class ports:
    # This class contains all default ev3 prot names
    outA = "ev3-ports:outA"
    outB = "ev3-ports:outB"
    outC = "ev3-ports:outC"
    outD = "ev3-ports:outD"

    in1 = "ev3-ports:in1"
    in2 = "ev3-ports:in2"
    in3 = "ev3-ports:in3"
    in4 = "ev3-ports:in4"

class led:
    # This class contains the names for the leds on the lego mindstorms brick
    leftGreen = 0
    leftRed = 1
    rightGreen = 2
    rightRed = 3

atexit.register(exit_handler) # register the exit handler
