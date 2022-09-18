from robot.brick import writeFile, readFile, devices

class sensor:
    def __init__(lego_sensor, address = "ev3-ports:in1"):
        lego_sensor.address = address
        devices[lego_sensor.address]["decimals"] = int(readFile(devices[lego_sensor.address]["path"] + "/decimals"))
        devices[lego_sensor.address]["num_values"] = int(readFile(devices[lego_sensor.address]["path"] + "/num_values"))
        devices[lego_sensor.address]["modes"] = readFile(devices[lego_sensor.address]["path"] + "/modes")
    
    def getRaw(lego_sensor):
        binData = readFile(devices[lego_sensor.address]["path"] + "/bin_data")
        binDataFormat = readFile(devices[lego_sensor.address]["path"] + "/bin_data_format")
        return binData, binDataFormat
    
    def sendcommand(lego_sensor, command):
        if command not in devices[lego_sensor.address]["modes"]:
            raise Exception("The mode: " + str(command) + " is not avalable for device: " + str(lego_sensor.address) + "accepted modes are: " + str(devices[lego_sensor.address]["modes"]))