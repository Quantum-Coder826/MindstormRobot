# brick.py
Attaching a motor is done with the following code:
```python
myMotor = motor(ports.outA)
```

## Methods

### `sendCommand(lego_motor, command)`
This method expects a command to be inputted as a string, [here](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#tacho-motor-subsystem) is a list of valid commands

### `getCountPerRot(lego_motor)`
Retuns a interger of the amount of tacho counts per one rotaion of the motor (360 degerees)

### `getCountPerMeter(lego_motor)`
Returns a interger of the amount of tacho counts it takes for the motor to travel 1 meter.

### `getFullTravel(lego_motor)`
Returns a interger of the full travel count of the motor in tacho counts.

### `driver(lego_motor)`
Returns the software driver name of the motor.

### `setDurty(lego_motor, duty)`
Sets the duty cyle the motor, the duty cycle can be a value from -100 to 100.

### `position(lego_motor)`
Retuns a interger that contains the current angele of the motor.

### `maxSpeed(lego_motor)`
Returns the maximum speed of the motor in tacho counts.

### `setPosition(lego_motor, angle)`
