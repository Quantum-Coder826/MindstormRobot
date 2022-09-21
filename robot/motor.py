#!/usr/bin/env python3

from robot.brick import writeFile, readFile
from os import listdir

class motor:
    def __init__(self, port):
        self.port = port
        for dir in listdir("/sys/class/tacho-motor"):
            if port == readFile("/sys/class/tacho-motor/" + str(dir) + "/address"):
                self.path = "/sys/class/tacho-motor/" + str(dir)

    def getPosition(self):
        return int(readFile(self.path + "/position"))

