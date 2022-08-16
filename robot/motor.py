"""
This file was made by Berend Veldthuis
the code is respolable for contorling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from robot.brick import writeFile, readFile, devices

class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address
    """
    TODO:
        ! sendcommand func
        ! run-to-abs-pos func
        ! run-to-rel-pos func
        ! run-timed func
        ! run-direct func
        ! stop func
        ! reset func

        * set duty cycle func
        * set position func
        * set speed func
        * get state func
        * set stop action
    """
    def setDuty(lego_motor, duty = 0):
        writeFile(devices[lego_motor.address]["path"] + "/duty_cycle_sp", duty)
    
    def setPostion(lego_motor, angle = 0):
        writeFile(devices[lego_motor.address]["path"] + "/postion_sp", angle)
    
    def setSpeed(lego_motor, speed = 0):
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)

    def getState(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/state")
    
    def stopMotor(lego_motor):
        writeFile(devices[lego_motor.address]["path"] + "/command", "stop")