use crate::robot::files;
use std::fs::read_dir;

// these function will handel the ev3 brick hardware
#[allow(dead_code)]
static  LED_PATHS:[&str; 4] = ["/sys/class/leds/led0:green:brick-status/brightness", "/sys/class/leds/led0:red:brick-status/brightness", "/sys/class/leds/led1:green:brick-status/brightness", "/sys/class/leds/led1:red:brick-status/brightness"];

// function for resetting the brick
pub fn init() {
    clear_led();
    set_led(0, 255);
    set_led(2, 255);
    
    let paths = read_dir("/sys/class/tacho-motor/").unwrap();

    for path in paths {
        let path: String = path.as_ref().unwrap().path().display().to_string() + "/command";
        files::write_str(&path, "reset");
    }
}

// TODO: add functions to read buttons

// functions for controlling the LED's
pub fn clear_led() {
    for led in LED_PATHS {
        files::write_int(led, &0);
    }
}

pub fn set_led(led: usize, value: u8) {
    let address: &str = LED_PATHS[led];
    files::write_int(address, &(value as i64));
}

