"""
This file was made by Berend Veldthuis
the code is respolable for contorling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from robot.brick import writeFile, readFile, devices

def setMode(port, mode): # sets the mode of a device
        if devices[port]["mode"] == str(mode):
            return True #exit if mode already set
        if mode not in readFile(devices[port]["path"] + "/commands"): # check and raise exception when a invalid mode is given
            raise Exception("The command: " + str(mode) + " is not avalable for device on: " + str(port) + "\navalable modes are: " + readFile(devices[port]["path"] + "/commands"))
        writeFile(devices[port]["path"] + "/command", mode) #update the mode
        devices[port]["mode"] = mode 

class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address
    