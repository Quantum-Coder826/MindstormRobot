from os import listdir

motorpath = "/sys/class/tacho-motor"
sensorpath = "/sys/class/lego-sensor"
ledpath = ["/sys/class/leds/led0:green:brick-status", "/sys/class/leds/led0:red:brick-status", "/sys/class/leds/led1:green:brick-status", "/sys/class/leds/led1:red:brick-status"]
devices = {}

# general functions
def readFile(path):
    f = open(str(path), "r")
    data = f.read()
    f.close()
    data = data.strip()  
    return str(data)

def writeFile(path, data):
    f = open(path, "w")
    f.write(str(data))
    f.close()

class mindstroms:
    def __init__(lego_brick):
        for dir in listdir(motorpath): #find all avalable motors and save the data
            devices[readFile(motorpath + "/" + str(dir) + "/address")] = {
                "path": str(motorpath + "/" +str(dir)),
                "driver_name": str(readFile(motorpath + "/" + str(dir) + "/driver_name")),
                "count_per_rot": str(readFile(motorpath + "/" + str(dir) + "/count_per_rot")),
                "max_speed": str(readFile(motorpath + "/" + str(dir) + "/max_speed")),
                "mode": None
            }
        
        for dir in listdir(sensorpath): #inf all avalable sensor and save the data
            devices[readFile(sensorpath + "/" + str(dir) + "/address")] = {
                "path": str(sensorpath + "/" + str(dir)),
                "driver_name": str(sensorpath + "/" + str(dir) + "/driver_name"),
                "decimals": str(sensorpath + "/" + str(dir) + "/decimals"),
                "num_values": str(sensorpath + "/" + str(dir) + "/num_values"),
                "mode": None
            }
        mindstroms.resetAll()
    
    def resetAll(): # resets all avalable motors, sensors don't need resetting
        for key in devices:
            if "out" in key:
                writeFile(devices[key]["path"] + "/command", "reset")
                devices[key]["mode"] = None
            else:
                continue

    def setLed(lego_brick, target = 0, value = 255): # changes the brightness of a led
        writeFile(ledpath[target] + "/brightness", value)

    # todo: figure out how the hell to read the buttons (https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ev3.html#buttons)

    # all the ports
    outA = "ev3-ports:outA"
    outB = "ev3-ports:outB"
    outC = "ev3-ports:outC"
    outD = "ev3-ports:outD"

    in1 = "ev3-ports:in1"
    in2 = "ev3-ports:in2"
    in3 = "ev3-ports:in3"
    in4 = "ev3-ports:in4"

class led:
    # led codes
    leftGreen = 0
    leftRed = 1
    rightGreen = 2
    rightRed = 3
