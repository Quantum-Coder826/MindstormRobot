# brick.rs
All methods in the brick.rs file are resposible for controlling the hardware on the lego mindstorms ev3 intelligent brick (45500).


## available metods and there use:
### ```init()```
Init initializes the brick it will set both green led's to full brightness and send the reset command to all connected motors. Also is adds a exit handeler what will do the same steps but on program termination.

### ```reset()```
Restets the brick

### ```exit()```
call this method to exit the program, it will call `brick::reset()` and terminate the program.

### ```keys() -> (u8, bool)```
this method retuns a thruple that contains a u8 wich is the unix keycode what was pressed, and the boolian is true when the key was registerd as being pressed down.

|Button|Value(u8)|
|---|---|
|Back|14|
|Center|28|
|Up|103|
|Left|105|
|Right|106|
|Down|108|

## Led's
all folling methods address contorlling the 4 led's on the brick. We call the led's by number in the following table:

|num|led|
|---|---|
|0|left green|
|1|left red|
|2|right green|
|3|right red|

### ```clear_led()```
This method will set the brighness of all led's to 0 turning them off

### ```set_led(Led: usize, value: u8)```
This method will set the brighness of a seleted led to the brightness of value. The lowest brighness is 0 and highes is 255.

## Battery
thes methods are to read the status fo the battery

### ```current_battery() -> f64```
will retun the current power being drawn from the battery in amps.

### ```is_LiIon() -> bool```
returns true when the LEGO Mindstorms EV3 Rechargeable Battery (95656) is used as the power source. If AA batterys are used it will return false.

### ```max_voltage_battery() -> f64```
retuns the maximum nominal battery voltage in volts. This value can be used to estamate the state of charge.

### ```min_voltage_battery() -> f64```
retuns the minimum nominal battery voltage in volts. This value can be used to estamate the state of charge.

### ```voltage_battery() -> f64```
retuns the amount of volt the battery is poviding. This value can be used to estamate the state of charge.