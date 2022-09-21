from robot.brick import readFile
gpio = "/dev/input/by-path/platform-gpio-keys.0-event"

while True:
    print(readFile(gpio))
    