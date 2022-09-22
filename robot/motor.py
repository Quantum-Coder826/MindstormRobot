#!/usr/bin/env python3

from robot.brick import writeFile, readFile
from os import listdir

class motor:
    def __init__(lego_motor, port):
        lego_motor.port = port
        for dir in listdir("/sys/class/tacho-motor"):
            if port == readFile("/sys/class/tacho-motor/" + str(dir) + "/address"):
                lego_motor.path = "/sys/class/tacho-motor/" + str(dir)

    def sendCommand(lego_motor, command):
        if command not in readFile(lego_motor.path + "/commands"):
            raise Exception("The command: " + command + " is not available for: " + str(lego_motor.path))
        writeFile(lego_motor.path + "command", str(command))
    
    def getCountPerRot(lego_motor):
        return int(readFile(lego_motor.path + "/count_per_rot"))
    
    def getCountPerMeter(lego_motor):
        return int(readFile(lego_motor.path + "/count_per_m"))
    
    def getFullTravel(lego_motor):
        return int(readFile(lego_motor.path + "/full_travel_count"))
    
    def driver(lego_motor):
        return readFile(lego_motor.path + "/driver_name")
    
    def setDuty(lego_motor, duty = 0):
        writeFile(lego_motor.path + "/duty_cycle_sp", int(duty))
    
    def getPosition(lego_motor):
        return int(readFile(lego_motor.path + "/position"))

    def maxSpeed(lego_motor):
        return int(readFile(lego_motor.path + "/max_speed"))
    
    def setPosition(lego_motor, angle = 0):
        writeFile(lego_motor.path + "/position_sp", int(angle))
    
    def speed(lego_motor):
        return int(readFile(lego_motor.path + "/speed"))
        


