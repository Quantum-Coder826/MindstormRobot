mod robot;
use robot::motor::Motor;

fn main() {
       let lage_Motor: Motor = Motor::attatch("ev3-ports:outA");
}