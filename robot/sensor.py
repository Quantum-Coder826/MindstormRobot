from robot.brick import writeFile, readFile, devices

class sensor:
    def __init__(lego_sensor, address = "ev3-ports:in1"):
        lego_sensor.address = address
