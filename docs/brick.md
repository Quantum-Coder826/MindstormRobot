# brick.rs
All methods in the brick.rs file are resposible for controlling the hardware on the lego mindstorms ev3 intelligent brick (45500).


### available metods and there use:
#### ```init()```
Init initializes the brick it will set both green led's to full brightness and send the reset command to all connected motors.

#### ```keys() -> (u8, bool)```
this method retuns a thruple that contains a u8 wich is the unix keycode what was pressed, and the boolian is true when the key was registerd as being pressed down.
