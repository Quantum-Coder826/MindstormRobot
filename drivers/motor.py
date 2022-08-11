"""
This file was made by Berend Veldthuis
the code is respolable for contorling lego motors 45502 and 2550113
The code is based on ev3dev: https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#sysfs
"""
from drivers.brick import writeFile, readFile, devices

class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address
    
    def getState(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/state")

    def getSpeed(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/speed")

    def setSpeed(lego_motor, speed = 0):
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)
    
    def setDuty(lego_motor, duty = 0):
        writeFile(devices[lego_motor.address]["path"] + "/duty_cycl_sp", duty)
    
    def setRamps(lego_motor, rampUp, rampDown):
        writeFile(devices[lego_motor.address]["path"] + "/ramp_up_sp", rampUp)
        writeFile(devices[lego_motor.address]["path"] + "/ramp_down_sp" , rampDown)
    
    def runRelPos(lego_motor, angle):
        writeFile(devices[lego_motor.address]["path"] + "/position_sp", angle)
    
    def runAbsPos(lego_motor, angle):
        writeFile(devices[lego_motor.address]["path"] + "/position_sp", angle)

    def runDuty(lego_motor, duty):
        writeFile(devices[lego_motor.address]["path"] + "/duty_cycle_sp", duty)
        writeFile(devices[lego_motor.address]["path"] + "/command", "run-direct")
    
    def runTimed(lego_motor, time, speed):
        writeFile(devices[lego_motor.address]["path"] + "/time_sp", time)
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)

    def setStopAction(lego_motor, stopAcion = "brake"):
        writeFile(devices[lego_motor.address]["path"] + "/stop_action", stopAcion)

    def stop(lego_motor):
        try: 
            writeFile(devices[lego_motor.address]["path"] + "/command", "stop")
            return True
        except: return False
    
    def reset(lego_motor):
        try:
            writeFile(devices[lego_motor.address]["path"] + "/command", "reset")
            return True
        except: return False