from drivers.brick import writeFile, readFile, devices

class sensor:
    def __init__(lego_sensor, port = "ev3-ports:in1"):
        lego_sensor.port = "ev3-ports:in" + str(port)
    
    @staticmethod
    def reload(target): #reloads a sensor attached to a given port
        devices[target]["decimals"] = readFile(devices[target]["path"] + "/decimals")
        devices[target]["num_values"] = readFile(devices[target]["path"] + "/num_values")

    def setMode(lego_sensor, mode):
        writeFile(devices[lego_sensor.port]["path"] + "/mode", mode)
        sensor.reload(lego_sensor.port)

    def getValue(lego_sensor, value = 0):
        data = int(readFile(devices[lego_sensor.port]["path"] + "/value" + str(value)))
        if devices[lego_sensor.port]["decimals"] == "1":
            return data / 10
        else:
            return data
    
    def getUnit(lego_sensor):
        return readFile(devices[lego_sensor.port]["path"] + "/units")