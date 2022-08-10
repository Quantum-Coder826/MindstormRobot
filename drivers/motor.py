
from brick import *

# class to control a motor
class motor:
    def __init__(lego_motor, port = "ev3-ports:outA"):
        lego_motor.port = "ev3-ports:out" + str(port)
    
    def getState(lego_motor):
        return readFile(devices[lego_motor.port]["path"] + "/state")

    def getSpeed(lego_motor):
        return readFile(devices[lego_motor.port]["path"] + "/speed")

    def runCommand(lego_motor, command, speed = 0, angle = 0, time = 0, duty = 0):
        writeFile(devices[lego_motor.port]["path"] + "/speed_sp", speed)
        writeFile(devices[lego_motor.port]["path"] + "/position_sp", angle)
        writeFile(devices[lego_motor.port]["path"] + "/time_sp", time)
        writeFile(devices[lego_motor.port]["path"] + "/duty_cycle_sp", duty)
        writeFile(devices[lego_motor.port]["path"] + "/command", command)
    
    def setStopAction(lego_motor, stopAcion = "brake"):
        writeFile(devices[lego_motor.port]["path"] + "/stop_action", stopAcion)

    def stop(lego_motor):
        try: 
            writeFile(devices[lego_motor.port]["path"] + "/command", "stop")
            return True
        except: return False
    
    def reset(lego_motor):
        try:
            writeFile(devices[lego_motor.port]["path"] + "/command", "reset")
            return True
        except: return False