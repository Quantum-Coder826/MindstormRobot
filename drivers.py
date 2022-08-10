#!/usr/bin/evn python3

# Code by Berend Veldthuis
# this file will contain all function and code to control the motors and sensors
# of the Lego mindstorm ev3, all of this code will make use of ev3dev and the
# low level dirver control and support linux provides.

# Ev3dev hardware level documentation: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/
from os import listdir

rootmotor = "/sys/class/tacho-motor"
rootsensor = "/sys/class/lego-sensor"
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
    f.write(str(data))
    f.close()


class brick:
    @staticmethod
    def configure(): # finds all connectet devices and create defaults
        for dir in listdir(rootmotor): #find all avalable motors and save the data
            devices[readFile(rootmotor + "/" + str(dir) + "/address")] = {
                "path": str(rootmotor + "/" +str(dir)),
                "driver_name": str(readFile(rootmotor + "/" + str(dir) + "/driver_name")),
                "count_per_rot": str(readFile(rootmotor + "/" + str(dir) + "/count_per_rot")),
                "max_speed": str(readFile(rootmotor + "/" + str(dir) + "/max_speed"))
            }
        
        for dir in listdir(rootsensor): #inf all avalable sensor and save the data
            devices[readFile(rootsensor + "/" + str(dir) + "/address")] = {
                "path": str(rootsensor + "/" + str(dir)),
                "driver_name": str(rootsensor + "/" + str(dir) + "/driver_name"),
                "decimals": str(rootsensor + "/" + str(dir) + "/decimals"),
                "num_values": str(rootsensor + "/" + str(dir) + "/num_values")
            }
        brick.resetAll()
    
    @staticmethod
    def resetAll():
        for key in devices:
            if "out" in key:
                writeFile(devices[key]["path"] + "/command", "reset")
            else:
                continue

# class to control a motor
class motor:
    def __init__(lego_motor, port = "ev3-ports:outA"):
        lego_motor.port = "ev3-ports:out" + str(port)
    
    def getState(lego_motor):
        return readFile(devices[lego_motor.port]["path"] + "/state")

    def getSpeed(lego_motor):
        return readFile(devices[lego_motor.port]["path"] + "/speed")

    def runCommand(lego_motor, command, speed = 0, angle = 0, time = 0, duty = 0):
        writeFile(devices[lego_motor.port]["path"] + "/speed_sp", speed)
        writeFile(devices[lego_motor.port]["path"] + "/position_sp", angle)
        writeFile(devices[lego_motor.port]["path"] + "/time_sp", time)
        writeFile(devices[lego_motor.port]["path"] + "/duty_cycle_sp", duty)
        writeFile(devices[lego_motor.port]["path"] + "/command", command)
    
    def stop(lego_motor):
        try: 
            writeFile(devices[lego_motor.port]["path"] + "/command", "stop")
            return True
        except: return False
    
    def reset(lego_motor):
        try:
            writeFile(devices[lego_motor.port]["path"] + "/command", "reset")
            return True
        except: return False
    



# todo make a class to read/contorl sensors
