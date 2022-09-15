"""
This file was made by Berend Veldthuis
the code is respolable for contorling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from robot.brick import writeFile, readFile, devices

def sendCommand(port, command): # sets the mode of a device
        if devices[port]["mode"] == str(command):
            return True #exit if mode already set
        if command not in readFile(devices[port]["path"] + "/commands"): # check and raise exception when a invalid mode is given
            raise Exception("The command: " + str(command) + " is not avalable for device on: " + str(port) + "\navalable modes are: " + readFile(devices[port]["path"] + "/commands"))
        writeFile(devices[port]["path"] + "/command", command) #update the mode
        devices[port]["mode"] = command

def atribute(port, attribte): # returns the concatanated path to selected file of a device
    return str(devices[port]["path"] + str(attribte))

class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address
        sendCommand(lego_motor.address, "reset")
    
    # all avalable control commands
    def runForever(lego_motor, speed = 0):
        writeFile(atribute(lego_motor.address, "speed_sp"), speed)
        sendCommand(lego_motor.address, "run-forever")
    
    def runAbsolutePos(lego_motor, speed = 0, position = 0):
        writeFile(atribute(lego_motor.address, "speed_sp"), speed)
        writeFile(atribute(lego_motor.address, "position_sp"), position)
        sendCommand(lego_motor.address, "run-to-abs-pos")
    
    def runRelativePos(lego_motor, speed = 0, position = 0):
        writeFile(atribute(lego_motor.address, "speed_sp"), speed)
        writeFile(atribute(lego_motor.address, "position_sp"), position)
        sendCommand(lego_motor.address, "run-to-rel-pos")

    def runTimed(lego_motor, speed = 0, time = 0):
        writeFile(atribute(lego_motor.address, "speed_sp"), speed)
        writeFile(atribute(lego_motor.address, "time_sp"), time)
        sendCommand(lego_motor.address, "run-timed")
    
    def runDuty(lego_motor, duty = 0):
        writeFile(atribute(lego_motor.address, "duty_sp"), duty)
        sendCommand(lego_motor.address, "run-direct")
    
    def stop(lego_motor):
        sendCommand(lego_motor.address, "stop")
        devices[lego_motor.address]["mode"] = None

    def reset(lego_motor):
        sendCommand(lego_motor.address, "reset")
        devices[lego_motor.address]["mode"] = None

    # data commands
    def getRotationCount(lego_motor):
        return int(readFile(atribute(lego_motor.address, "count_per_rot")))
    
    def getMeterCount(lego_motor):
        return int(readFile(atribute(lego_motor.address, "count_per_m")))
    
    def getFullTravel(lego_motor):
        return int(readFile(atribute(lego_motor.address, "full_travel_count")))
    
    def getPosition(lego_motor):
        return int(readFile(atribute(lego_motor.address, "position")))
    
    def getSpeed(lego_motor):
        return int(readFile(atribute(lego_motor.address, "speed")))
    