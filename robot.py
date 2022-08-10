#!/usr/bin/env python3
# * python3 /home/robot/robot/robot.py


from os import listdir
import sys, threading


polling = threading.Event(); polling.set()
ready = threading.Event(); ready.clear()
rootmotor = "/sys/class/tacho-motor/"
rootsensor = "/sys/class/lego-sensor/"
dev = {}

# sensor/motor postion I/O thread
def pullData():
    t = threading.current_thread()
    while getattr(t, "run", True):
        polling.wait(timeout=5)
        ready.clear()
        for key in dev:
            if rootmotor in dev[key]["path"]: # is motor?
                dev[key]["position"] = int(readFile(str(dev[key]["path"]) + "/position"))
                dev[key]["speed"] = int(readFile(str(dev[key]["path"]) + "/speed"))

            elif rootsensor in dev[key]["path"]: #is sensor
                for i in range(0,dev[key]["num_values"],1): # loop door de meerdere outputs
                    dev[key]["decimals"] = int(readFile(dev[key]["path"] + "/decimals"))
                    value = readFile(str(dev[key]["path"]) + "/value" + str(i))
                    if dev[key]["decimals"] == 1: #add decimal
                        value = float(value) / 10
                        dev[key]["value" + str(i)] = float(value)
                    else:
                        dev[key]["value" + str(i)] = value
        ready.set()


# general functions
def readFile(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    data = data.strip()  
    return data

def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()

def resetMotors(): # reset all available motors
    for key in dev:
        if rootmotor in dev[key]["path"]: # is motor?
            writeFile(str(dev[key]["path"]) + "/command", "reset")



if __name__ == "__main__": #start main thread
    for dir in listdir(rootmotor): # get all conected motors (setup)
        dev[readFile(rootmotor + str(dir) + "/address")] = {
            "path": str(rootmotor + str(dir)),
            "driver": readFile(rootmotor + str(dir) + "/driver_name"),
            "position": int(0),
            "speed": int(0)
        }
    
    for dir in listdir(rootsensor): # get all conected sensors
        dev[readFile(rootsensor + str(dir) + "/address")] = {
            "path": str(rootsensor + str(dir)),
            "decimals": int(readFile(rootsensor + str(dir) + "/decimals")),
            "num_values": int(readFile(rootsensor + str(dir) + "/num_values")),
            "value": int(0)
        }
    

    th = threading.Thread(target=pullData)
    th.start()
    # main code/vars
    resetMotors()
    writeFile(str(dev["ev3-ports:outA"]["path"]) + "/command", "run-direct")
    writeFile(str(dev["ev3-ports:outD"]["path"]) + "/command", "run-direct")
    writeFile(str(dev["ev3-ports:in4"]["path"]) + "/mode", "US-DIST-CM")
    try: 
        while True: # main code loop
            polling.set()
            ready.wait()
            polling.clear()
            if dev["ev3-ports:in4"]["value0"] <= 10:
                writeFile(str(dev["ev3-ports:outA"]["path"]) + "/duty_cycle_sp", "50")
                writeFile(str(dev["ev3-ports:outD"]["path"]) + "/duty_cycle_sp", "-50")
            else:
                writeFile(str(dev["ev3-ports:outA"]["path"]) + "/duty_cycle_sp", "50")
                writeFile(str(dev["ev3-ports:outD"]["path"]) + "/duty_cycle_sp", "50")

    except KeyboardInterrupt:
            print("stopping")
            th.run = False
            th.join()
            resetMotors()
            sys.exit(0)