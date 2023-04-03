mod robot;
use robot::brick;

fn main() {
       brick::init();
       println!("{}", brick::max_voltage_battery());
       println!("{}", brick::min_voltage_battery());
       println!("{}", brick::voltage_battery());
       println!("{}", brick::current_battery());
       println!("{}", brick::is_LiIon());      
}