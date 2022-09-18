from robot.brick import writeFile, readFile, devices

class sensor:
    def __init__(lego_sensor, address = "ev3-ports:in1"):
        lego_sensor.address = address
        devices[lego_sensor.address]["decimals"] = int(readFile(devices[lego_sensor.address]["path"] + "/decimals"))
        devices[lego_sensor.address]["num_values"] = int(readFile(devices[lego_sensor.address]["path"] + "/num_values"))
        devices[lego_sensor.address]["modes"] = readFile(devices[lego_sensor.address]["path"] + "/modes")
    
    def getRaw(lego_sensor):
        file = open(devices[lego_sensor.address]["path"] + "/bin_data", "rb")
        binData = file.read()
        del file
        binDataFormat = readFile(devices[lego_sensor.address]["path"] + "/bin_data_format")
        return binData, binDataFormat
    
    def setMode(lego_sensor, mode):
        if mode not in devices[lego_sensor.address]["modes"]:
            raise Exception("The mode: " + str(mode) + " is not avalable for device: " + str(lego_sensor.address) + "accepted modes are: " + str(devices[lego_sensor.address]["modes"]))
        writeFile(devices[lego_sensor.address]["path"] + "/mode", mode)
        devices[lego_sensor.address]["decimals"] = int(readFile(devices[lego_sensor.address]["path"] + "/decimals"))
        devices[lego_sensor.address]["num_values"] = int(readFile(devices[lego_sensor.address]["path"] + "/num_values"))

    def getUnits(lego_sensor):
        return readFile(devices[lego_sensor.address]["path"] + "/units")
    
    def getValue(lego_sensor, value = 0):
        if value > devices[lego_sensor.address]["num_values"]:
            raise Exception("You tried to get a value that is not avalable try again. port: " + str(lego_sensor.address) + " mode: " + str(readFile(devices[lego_sensor.address]["path"] + "/mode")))
        value = int(readFile(devices[lego_sensor.address]["path"] + "/value" + str(value)))
        if devices[lego_sensor.address]["decimals"] == 0:
            return value
        value = value / 10
        return value

    # sensor specific functions
    def getButton(lego_sensor):
        if int(readFile([lego_sensor.address]["path"] + "/value0")) == 1:
            return True
        else:
            return False
