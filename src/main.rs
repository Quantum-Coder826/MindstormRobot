mod brick;

fn main() {
    let battery_amps = brick::battery_current();
    print!("{battery_amps}");
}