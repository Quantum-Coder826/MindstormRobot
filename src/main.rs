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
            println!("right");
        } else if heading < -2 {
            println!("left");
        } else {
            println!("middle");
        }
    }
}