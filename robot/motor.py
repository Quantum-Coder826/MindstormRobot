#!/usr/bin/env python3

from robot.brick import writeFile, readFile
from os import listdir

class motor:
    def __init__(self, port):
        self.port = port
        for dir in listdir("/sys/class/tacho-motor"):
            if port == readFile("/sys/class/tacho-motor/" + str(dir) + "/address"):
                self.path = "/sys/class/tacho-motor/" + str(dir)

    def sendCommand(self, command):
        if command not in readFile(self.path + "/commands"):
            raise Exception("The command: " + command + " is not available for: " + str(self.path))
        writeFile(self.path + "command", str(command))
    
    def getCountPerRot(self):
        return int(readFile(self.path + "/count_per_rot"))
    
    def getCountPerMeter(self):
        return int(readFile(self.path + "/count_per_m"))
    
    def getFullTravel(self):
        return int(readFile(self.path + "/full_travel_count"))
    
    def driver(self):
        return readFile(self.path + "/driver_name")
    
    def setDuty(self, duty = 0):
        writeFile(self.path + "/duty_cycle_sp", int(duty))
    
    def getPosition(self):
        return int(readFile(self.path + "/position"))

    def maxSpeed(self):
        return int(readFile(self.path + "/max_speed"))
    
    def setPosition(self, angle = 0):
        writeFile(self.path + "/position_sp", int(angle))
    
    def speed(self):
        return int(readFile(self.path + "/speed"))
        


