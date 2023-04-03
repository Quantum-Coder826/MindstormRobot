use crate::robot::files;

// these function will handel the ev3 brick hardware
#[allow(dead_code)]
static  LED_PATHS:[&str; 4] = ["/sys/class/leds/led0:green:brick-status/brightness", "/sys/class/leds/led0:red:brick-status/brightness", "/sys/class/leds/led1:green:brick-status/brightness", "/sys/class/leds/led1:red:brick-status/brightness"];

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

