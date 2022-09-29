# MindstormRobot
 Use python to control a lego mindstorms ev3

The base file looks like this:
```python
from robot.brick import *
from robot.motor import *
from robot.sensor import *

brick = mindstorms()
```

# Brick.py
Brick.py contains the mindstorms, ports and led class.

## Class `ports`
is used to address devices, it just reflects the portname on the physical robot
so ```ports.outA``` refers to port A on the mindstorms brick.

## Class `led`
is used to address the 4 leds on the brick, the adressing is the following:
target | place | color
--- | --- | ---
0 | left | green
1 | left | red
2 | right | green
3 | right | red

## Class `mindstorms(port)`
### Method `setLed(target = 0, value = 255)`
`target` contains the led, addressing led's is done via the led class
`value` is the brightness of the led is go's form 0 to 255.

# motor.py
motor.py contains all necessary code to run the lego mindstorms tacho motors.
## Class `motor(port)`
The motor class contain all the methods to control lego tacho motors, the class expects a port number to be inputted.

### Method `sendCommand(lego_motor, command)`
sends a command to the motor possible commands are:
<div style="with:500px">command</div> | description
--- | --- 
`"run-forerver"` | Causes the motor to run until another command is sent.
`"run-to-abs-pos"` | Runs the motor to an absolute position specified by`position_sp` and then stops the motor using the command specified in `stop_action`
`"run-to-rel-pos"` | Runs the motor to a position relative to the current position value. The new position will be current `position` + `position_sp`. When the new position is reached, the motor will stop using the command specified by `stop_action`.
`"run-timed"` | Run the motor for the amount of time specified in `time_sp` and then stops the motor using the command specified by `stop_action`.
`"run-direct"` | Runs the motor using the duty cycle specified by `duty_cycle_sp`. Unlike other run commands, changing `duty_cycle_sp` while running will take effect immediately.
### Usefule code snippets:
Tankdrive keymap for use with controller:

```python
[(0,0),(50,0),(-50,0),(0,50),(0,-50),(50,50),(50,-50),(-50,50),(-50,-50),(0,0),(0,0),(0,0)]
```