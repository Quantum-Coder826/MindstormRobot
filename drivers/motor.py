
from drivers.brick import writeFile, readFile, devices

# class to control a motor
class motor:
    def __init__(lego_motor, address = "ev3-ports:outA"):
        lego_motor.address = address
    
    def getState(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/state")

    def getSpeed(lego_motor):
        return readFile(devices[lego_motor.address]["path"] + "/speed")

    def runCommand(lego_motor, command, speed = 0, angle = 0, time = 0, duty = 0):
        writeFile(devices[lego_motor.address]["path"] + "/speed_sp", speed)
        writeFile(devices[lego_motor.address]["path"] + "/position_sp", angle)
        writeFile(devices[lego_motor.address]["path"] + "/time_sp", time)
        writeFile(devices[lego_motor.address]["path"] + "/duty_cycle_sp", duty)
        writeFile(devices[lego_motor.address]["path"] + "/command", command)
    
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