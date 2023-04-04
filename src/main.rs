mod robot;
use robot::brick;
use robot::sensor::Sensor;

fn main() {
       brick::init();

       let sonar = Sensor::attatch(&Ports.in1);
       println!("{}", sonar.name);

}