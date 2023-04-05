mod robot;
use robot::brick::brick;
use robot::files;

fn main() {
    brick::init();
    
    let data: Vec<u8> = files::read_bytes("/dev/input/event1");
    println!("got data");
    for byte in data {
        println!("{}", byte);
    }
}