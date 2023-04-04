mod robot;
use robot::brick::brick;
use robot::files;

fn main() {
    brick::init();
    loop {
        let data = files::read_bytes("/dev/input/by-path/platform-gpio-keys.0-event");
        println!("{:?}", data);
    }
}