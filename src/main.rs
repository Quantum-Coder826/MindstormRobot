mod robot;
use robot::brick;
use  robot::motor::Motor;

fn main() {
       brick::init();

       let myMotor = Motor::attatch("ev3-ports:outA");
       myMotor.run_duty(120);

}