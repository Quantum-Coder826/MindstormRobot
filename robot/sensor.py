from robot.brick import writeFile, readFile
from os import listdir

class sensor:
    def __init__(lego_sensor, port):
        lego_sensor.port = port
        for dir in listdir("/sys/class/lego-sensor"):
            if port == readFile("/sys/class/lego-sensor/" + str(dir) + "/address"):
                lego_sensor.path = "/sys/class/lego-sensor/" + str(dir)

    def getBin(lego_sensor):
        f = open(lego_sensor.path + "/bin_data", "rb")
        data = f.read()
        f.close()
        data_format = readFile(lego_sensor.path + "/bin_data_format")
        return data, data_format

    def driver(lego_sensor):
        return readFile(lego_sensor.path + "/driver_name")
    
    def setMode(lego_sensor, mode):
        if mode not in readFile(lego_sensor.path + "/modes"):
            raise Exception("The mode: " + str(mode) + " for device: " + str(lego_sensor.port) + " is not available")
        else:
            writeFile(lego_sensor.path + "/mode", mode)

    def getUnits(lego_sensor):
        return str(readFile(lego_sensor.path + "/units"))
    
    def getValue(lego_sensor, value = 0):
        if value > int(readFile(lego_sensor.path + "/num_values")):
            raise Exception("the value: " + str(value) + " for device: " + str(lego_sensor.port) + " is not available")
        else:
            return int(readFile(lego_sensor.path + "/value" + str(value)))