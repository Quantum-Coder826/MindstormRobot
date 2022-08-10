#!/usr/bin/evn python3

# Code by Berend Veldthuis
# this file will contain all function and code to control the motors and sensors
# of the Lego mindstorm ev3, all of this code will make use of ev3dev and the
# low level dirver control and support linux provides.

# Ev3dev hardware level documentation: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/
from os import listdir

rootmotor = "/sys/class/tacho-motor"
rootsensor = "/sys/class/lego/sensor"
devices = {}

# general functions
def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    data = data.strip()  
    return data

def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
