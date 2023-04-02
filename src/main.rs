mod brick;

fn main() {
    println!("{}", brick::file_read_int("/sys/class/tacho-motor/motor0/position"));
}