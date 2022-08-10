from os import listdir

rootmotor = "/sys/class/tacho-motor"
rootsensor = "/sys/class/lego-sensor"
devices = {}

# general functions
def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    data = data.strip()  
    return data

def writeFile(path, data):
    f = open(path, "w")
    f.write(str(data))
    f.close()

class brick:
    @staticmethod
    def configure(): # finds all connectet devices and create defaults
        for dir in listdir(rootmotor): #find all avalable motors and save the data
            devices[readFile(rootmotor + "/" + str(dir) + "/address")] = {
                "path": str(rootmotor + "/" +str(dir)),
                "driver_name": str(readFile(rootmotor + "/" + str(dir) + "/driver_name")),
                "count_per_rot": str(readFile(rootmotor + "/" + str(dir) + "/count_per_rot")),
                "max_speed": str(readFile(rootmotor + "/" + str(dir) + "/max_speed"))
            }
        
        for dir in listdir(rootsensor): #inf all avalable sensor and save the data
            devices[readFile(rootsensor + "/" + str(dir) + "/address")] = {
                "path": str(rootsensor + "/" + str(dir)),
                "driver_name": str(rootsensor + "/" + str(dir) + "/driver_name"),
                "decimals": str(rootsensor + "/" + str(dir) + "/decimals"),
                "num_values": str(rootsensor + "/" + str(dir) + "/num_values")
            }
        brick.resetAll()
    
    @staticmethod
    def resetAll():
        for key in devices:
            if "out" in key:
                writeFile(devices[key]["path"] + "/command", "reset")
            else:
                continue
