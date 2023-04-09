# motor.rs
All methods in the motor.rs file are used to contorl the following motors:
- LEGO White Mindstorms EV3 Large Motor (95658)
- LEGO Medium Stone Gray Mindstorms EV3 Medium Motor (99455)

More information can be foun ton the ev3dev [site](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/motors.html#tacho-motor-subsystem) that gives more context about everything that is happening in the backgound.

## the methods
### ```attatch(port: &str) -> Motor```
This method is required to interact wich a motor, it retuns the struct Motor what will contain all the information all other metods need to work. The port variable sould look someting like `ev3-ports:out<X>`
Where X is the letter the phisical device is connecte to.

### ```run_forever(&self, speed_sp: i16)```
This command will command the motor to run continuously at the given `speed_sp` until another command is issued.

### ```run_abs_pos(&self, angle_sp: i16, speed_sp: i16)```
The motor will run to the specifided angel with the specified speed and stop using the stop action that is set.

### ```run_rel_pos(&self, angle_sp: i16, speed_sp: i16)```
Same as `run_abs_pos` but the new postion will be the current position + `angel_sp`.

### ```run_rot_count(&self, count: u8, speed_sp: i16)```
Make the motor turn for a specified amount of full rotations and stops the motor using the specified stop action.

### ```run_timed(&self, time_sp: u64, speed_sp: i16)```
Runs the motor for a amount of seconds specified in `time_sp`.

### ```run_duty(&self, duty_sp: i8)```
Run the motor on a set duty cycle, the value in `duty_sp` ranges form -100 to 100.

### ```stop(&self)```
stops the motor using the set stop action.

### ```reset(&self)```
Resets the motor if the motor is running it will stop running and all values will be set to default.

### ```postion(&self) -> i64```
retuns the current postion in encoder counts use the `count_per_rot` field in the `Motor` struct to convert to degrees. For the offial lego motors this value will already be in degrees.

### ```speed(&self) -> i64```
retusn the current speed of the motor in encoder counts per second use the `count_per_rot` field in the `Motor` struct to convert to degrees per second.

### ```state(&self) -> String```
Will return the motor state under is a table of what it all means.
|return|description|
|---|---|
|running|Power is being sent to the motor.|
|ramping|The motor is ramping up or down and has not yet reached a constant output level.|
|holding|The motor is trying to hold a fixed postion.
|overloaded|The motor is turning as fast as possible, but cannot reach its `speed_sp`|
|stalled|The motor is trying to run but is not turning at all.|

### ```set_stop_action(&self, action: &str)```
This method will set the stop action of the motor there are mutible values:
|action|description|
|---|---|
|coast|Removes power from the motor. The motor will freely coast to a stop.|
|brake|Actively try to stop the motor|
|hold|The motor will brake, and actively try to stay on it's current postions.|