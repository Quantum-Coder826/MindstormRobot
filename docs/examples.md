# Examples
Here are a series of useful examples and snippets that can be used in your code.

## Tankdrive
A simple tankdrive implimentation using 2 lage motors, the ir sensor and remote.
``` rust
mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();

    let keys_remote: [[i8; 2]; 12] = [[0,0],[50,0],[-50,0],[0,50],[0,-50],[50,50],[50,-50],[-50,50],[-50,-50],[0,0],[0,0],[0,0]];

    let left_motor: Motor = Motor::attatch("ev3-ports:outB");
    let right_motor: Motor = Motor::attatch("ev3-ports:outC");
    
    let mut ir: Sensor = Sensor::attatch("ev3-ports:in4");
    ir.set_mode("IR-REMOTE");

    loop {
        let key: usize = match ir.get_value(0) {
            SensorReturn::Int(key) => key as usize,
            SensorReturn::Float(_) => 0// eg do nothig
        };

        left_motor.run_duty(keys_remote[key][0]);
        right_motor.run_duty(keys_remote[key][1]);
    }
}
```

the first useful snippet that can be found here is:
``` rust
let keys_remote: [[i8; 2]; 12] = [[0,0],[50,0],[-50,0],[0,50],[0,-50],[50,50],[50,-50],[-50,50],[-50,-50],[0,0],[0,0],[0,0]];
```
this array countans duty values for a trankrive motor setup.

## Seeker
This simple program uses the `IR-SEEK` mode of the ir sensor to keep 'looking at' a ir remote with the beacon turned on.
``` rust
mod robot;
use robot::brick::brick;
use robot::motor::Motor;
use robot::sensor::{Sensor, SensorReturn};

fn main() {
    brick::init();

    let left_motor: Motor = Motor::attatch("ev3-ports:outB");
    let right_motor: Motor = Motor::attatch("ev3-ports:outC");

    let mut ir: Sensor = Sensor::attatch("ev3-ports:in4");
    ir.set_mode("IR-SEEK");

    loop {
        let heading: i64 = match  ir.get_value(0) {
            SensorReturn::Int(heading) => heading,
            SensorReturn::Float(_) => 0
        };

        if heading > 2 {
            left_motor.run_duty(20);
            right_motor.run_duty(-20);
        } else if heading < -2 {
            left_motor.run_duty(-20);
            right_motor.run_duty(20);
        } else {
            left_motor.run_duty(0);
            right_motor.run_duty(0);
        }

    }
}
```