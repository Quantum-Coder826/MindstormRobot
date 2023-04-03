mod robot;
use robot::motor::Motor;

fn main() {
       let lageMotor: Motor = Motor::attatch("ev3-ports:outA");
}