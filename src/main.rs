mod robot;
use robot::brick;
use robot::sensor::Sensor;

fn main() {
       brick::init();

       let sonar = Sensor::attatch("ev3-ports:in4");
       println!("{}", sonar.name);

}