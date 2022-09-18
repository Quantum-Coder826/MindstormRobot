"""
This file was made by Berend Veldthuis
the code is respolable for controlling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from robot.brick import writeFile, readFile, devices

class motor:
    def __init__(lego_motor, address):
        lego_motor.address = address
        devices[lego_motor.address]["count_per_rot"] = int(readFile(devices[lego_motor.address]["path"] + "/count_per_rot"))
        devices[lego_motor.address]["commands"] = str(readFile(devices[lego_motor.address]["path"] + "/commands"))
        devices[lego_motor.address]["max_speed"] = int(readFile(devices[lego_motor.address]["path"] + "/max_speed"))
    
    def sendCommand(lego_motor, command):
        if command not in devices[lego_motor.address]["commands"]:
            raise Exception("The command: " + str(command) + " is not avalable for device: " + str(lego_motor.address) + "acepted commads are: " + str(devices[lego_motor.address]["commands"]))
        writeFile(devices[lego_motor.address]["path"] + "/command", command)
    
    def getTravelCount(lego_motor):
        return int(readFile(devices[lego_motor.address]["path"] + "/full_travel_count"))
    
    def setDuty(lego_motor, duty = 0):
        writeFile(devices[lego_motor.address]["path"] + "/duty_sp", duty)
    
    def getPosition(lego_motor):
        return int(readFile(devices[lego_motor.address]["path"] + "/position"))
    
    def setPosition(lego_motor, angle = 0):
        writeFile(devices[lego_motor.address]["path"] + "/position_sp", angle)
    
    def getSpeed(lego_motor):
        return int(readFile(devices[lego_motor.address]["path"] + "/speed"))
    
    def setSpeed(lego_motor, speed = 0):
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)
    
    def getState(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/stop_action")
    
    def setTime(lego_motor, time = 0):
        writeFile(devices[lego_motor.address]["path"] + "/time_sp", time)
    
    def getTime(lego_motor):
        return int(readFile(devices[lego_motor.address]["path"] + "/time_sp"))
