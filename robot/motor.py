"""
This file was made by Berend Veldthuis
the code is respolable for contorling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from robot.brick import writeFile, readFile, devices

class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address

    def setDuty(lego_motor, duty = 0):
        writeFile(devices[lego_motor.address]["path"] + "/duty_cycle_sp", duty)
    
    def setPostion(lego_motor, angle = 0):
        writeFile(devices[lego_motor.address]["path"] + "/postion_sp", angle)
    
    def setSpeed(lego_motor, speed = 0):
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)

    def getState(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/state")
    
    def setStopAction(lego_motor, action):
        writeFile(devices[lego_motor.address]["path"] + "/stop_action", action)
    
    def stopMotor(lego_motor):
        writeFile(devices[lego_motor.address]["path"] + "/command", "stop")
    
    def runAbs(lego_motor, angle = 0):
        writeFile(devices[lego_motor.address]["path"] + "/postions_sp", angle)
        writeFile(devices[lego_motor.address]["path"] + "/command", "run-to-abs-pos")
    
    def runRel(lego_motor, angle = 0):
        motor.setPostion(lego_motor.address, angle)
        writeFile(devices[lego_motor.address]["path"] + "/command", "run-to-rel-pos")
    
    def runTimed(lego_motor, time = 0):
        writeFile(devices[lego_motor.address]["path"] + "/time_sp", time)
        writeFile(devices[lego_motor.address]["path"] + "/command", "run-timed")
    
    def runDirect(lego_motor, duty = 0):
        motor.setDuty(lego_motor.address, duty)
        writeFile(devices[lego_motor.address]["path"] + "/command", "rund-direct")

class tankDrive:
    def __init__(lego_motor, leftMotor, rightMotor):
        lego_motor.leftMotor = leftMotor
        lego_motor.rightMotor = rightMotor
    
    def drive(dutyRight, dutyLeft):
        
