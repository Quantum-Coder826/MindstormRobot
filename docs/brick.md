# brick.py
This file contains all methots to contol the lego mindstorms ev3 interligent brick. And also contains some classe that refer to the default hardware of the brick. 

When creating a new program it is recomenden to create a object of the mindstorms class by:
```python
brick = mindstorms()
```
By doing this you can use the methods in the class with the object brick and when creating the brick object the ev3 brick will be reset by stopping resetting all conected motors and setting both led's to green.

## Methods
The following methods are for contrilling the ev3 intelligent brick or collecting data.

### Led
Methods for controlling the 4 led's on the ev3 brick. There are 2 green and 2 red led's.

#### `setLed(lego_brick, target, value)`
`setLed` will set the brightness value of an led on the brick, target is an interger refering to wich led will be writte to. The value is the brighness of the led form 0 (compleatly off) to 255 (compleatly on) You can use the class `led` to select a led on the front panel.

#### `clearLeds(lego_brick)`
Will turn off all led's by setting there brightness to 0.

#### `resetLeds(lego)brick)`
Will turn off the red led's and turnt both green led's to full brightness.

### keys
This method will read all keys on the brick, this does not count for push-buttons connected to imput port. It only handles inpot form the 6 face keys.

#### `getKey(lego_brick)`
When this method is calld it will wait until a key on the brick is pressed or relesed. It will return two values a integer wicht contains the keycode and a bolian wich is True when a key was pressed and False when a key is realesed. The extra data class `keys` can be used to identify keypresses.
The keycodes are:
|Button|Keycode (int)|
|---|---|
|Back|14|
|Center|28|
|Up|103|
|Left|105|
|Right|106|
|Down|108|

### Battery
The ev3 brick has a battery so it may be useful to read its status, the following methods acomplish that.

#### `batteryCurrent(leg_brick)`
This function will return the current drawn from the battery in amps.

#### `isLiIon(lego_brick)`
This function will return True if the battery installed in the brick is a lego 95656 Lithhium Ion rechargeable battery pack. Else it will return False.

#### `maxBatteryVoltage(lego_brick)`
Returns the maximum battery voltage of the battery in volts.

#### `minBatteryVoltage(lego_brick)`
Returns the minimum battery voltage of the battery in volts.

#### `batteryVoltage(lego_brick)`
Returns the current battery voltage of the battery in volts.

### Extra classes
Tere are a few extra classes in brick.py and they can be used to more easaly address ports and leds and read key inputs.

#### Class ports
The class ports contains all internal port names of the ports the ev3 inteligent brick already has. so when connecting a sensor on port 4 you do someting like this:
```python
mysensor = sensor(ports.in4)
```
As normal with the hardware you can only connect sensors to number ports and motors to letter ports.

#### Class led
This class allows you to easaly contorl the leds on the brick. Using it is quite self explanitory:
```python
    brick.setLed(led.leftGreen, 255)
```
This code will turn the left green led to its full brightness

#### Class key
Allows you to more easaly read the keycodes in your code. The code to detect the center key being pressed sould be something like this:
```python
if brick.getKey() == key.Enter:
    # do something
```
