#!/usr/bin/env python3

from robot.brick import writeFile, readFile, devices
from os import listdir

class motor:
    def __init__(lego_motor, address):
        lego_motor.address = address
        for dir in listdir("/sys/class/tacho-motor"):
            if dir != address:
                continue
            elif dir == address:
                devices[address]["path"] = "/sys/class/tacho-motor" + str(dir)

    