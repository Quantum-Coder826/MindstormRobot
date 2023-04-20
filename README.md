# MindstormRobot
Use rust to contorl a lego mindstorms ev3

# Setup
Using this script/libary requirs to download te repo (the docs folder is not requied) you can write your code in the `main.rs` file and build and upload it to a lego Mindostorms ev3. It is recomende to whave cargo installed. A base `main.rs` should look like the following;
```rust
mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();
}
```
# Docs
the documentation is broken down in separate pages for each file of the program. All file can be found here:
- [brick.rs](/docs/brick.md)
- [motor.rs](/docs/motor.md)
- [sensor.rs](/docs/sensor.md)

More exsamples and snippets can be found [here](/docs/examples.md)

Not all files are coverd this is due to these files not containing essential information about using this codebase to program a lego mindstorms ev3.


### todo's
- [ ] Change sensor.get_value to have separeate functions for retuning ints or floats