mod brick;

fn main() {
    brick::write_to_file("/sys/class/tacho-motor/motor0/command", b"reset");

    while true {
        let pos:String = brick::read_from_file("/sys/class/tacho-motor/motor0/position");
        println!("{pos}");
    }
}