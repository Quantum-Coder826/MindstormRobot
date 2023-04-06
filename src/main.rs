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