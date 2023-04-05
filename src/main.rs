mod robot;
use robot::brick::brick;
use robot::files;

fn main() {
    brick::init();
    loop {
        let data: Vec<u8> = files::read_bytes("/dev/input/by-path/platform-gpio_keys-event", 32);
        println!("Button: {:?}", data);
    }
}