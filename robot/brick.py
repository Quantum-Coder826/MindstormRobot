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

class mindstorms:
    def __init__(lego_brick):
        for dir in listdir("/sys/class/tacho-motor"):
            devices[readFile("/sys/class/tacho-motor/" + str(dir) + "/address")] = {
                "path": "/sys/class/tacho-motor/" + str(dir),
                "driver_name": readFile("/sys/class/tacho-motor/" + str(dir) + "/driver_name")
            }
        
        for dir in listdir("/sys/class/lego-sensor"):
            devices[readFile("/sys/class/lego-sensor/" + str(dir) + "/address")] = {
                "path": "/sys/class/lego-sensor/" + str(dir),
                "driver_name": readFile("/sys/class/lego-sensor/" + str(dir) + "/driver_name")
            }
        mindstorms.resetAll()
        print(devices)
    
    def resetAll(): #sensors don't need resetting
        for key in devices:
            if "out" in key:
                writeFile(devices[key]["path"] + "/command", "reset")
                devices[key]["mode"] = None
            else:
                continue
        writeFile(ledpath[0] + "/brightness", 255)
        writeFile(ledpath[1] + "/brightness", 0)
        writeFile(ledpath[2] + "/brightness", 255)
        writeFile(ledpath[3] + "/brightness", 0)

    def setLed(lego_brick, target = 0, value = 255): # changes the brightness of a led
        writeFile(ledpath[target] + "/brightness", value)

    # todo: figure out how the hell to read the buttons (https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ev3.html#buttons)
class ports:
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
