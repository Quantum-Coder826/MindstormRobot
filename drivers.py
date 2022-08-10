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

# todo find all sensors and motors (use a class)
class brick:
    def __init__(ev3):
        pass

    def configure():
        for dir in listdir(rootmotor): #find all avalable motors and save the data
            devices[readFile(rootmotor + str(dir) + "/address")] = {
                "path": str(rootmotor + str(dir)),
                "driver_name": str(readFile(rootmotor + str(dir) + "/driver_name")),
                "count_per_rot": str(readFile(rootmotor + str(dir) + "/count_per_rot")),
                "max_speed": str(readFile(rootmotor + str(dir) + "/max_speed"))
            }
        
        for dir in listdir(rootsensor): #inf all avalable sensor and save the data
            devices[readFile(rootsensor + str(dir) + "/address")] + {
                "path": str(rootsensor + str(dir)),
                "driver_name": str(rootsensor + str(dir) + "/driver_name"),
                "decimals": str(rootsensor + str(dir) + "/decimals"),
                "num_values": str(rootsensor + str(dir) + "/num_values")
            }


# todo make a class to read/control motors
# todo make a class to read/contorl sensors
