from robot.brick import writeFile, readFile, devices

def setMode(port, mode):
    if mode not in readFile(atribute(port, "modes")):
        raise Exception("The mode: " + mode + " is not avalabe for device on: " + port + "\navalable modes are: " + readFile(atribute(port, "modes")))
    if mode == readFile(atribute(port, "mode")):
        return True
    writeFile(atribute(port, "mode"), mode)

def atribute(port, file):
    return devices[port]["path"] + file

class sensor:
    def __init__(lego_sensor, address = "ev3-ports:in1"):
        lego_sensor.address = address
        