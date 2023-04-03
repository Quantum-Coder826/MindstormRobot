use crate::robot::files;

// these function will handel the ev3 brick hardware

// TODO: add functions to read buttons

// functions for controlling the LED's
pub fn clear_led() {
    let led_paths:[&str; 4] = ["/sys/class/leds/led0:green:brick-status", "/sys/class/leds/led0:red:brick-status", "/sys/class/leds/led1:green:brick-status", "/sys/class/leds/led1:red:brick-status"];
    for led in led_paths {
        files::write_int(led, &0);
    }
}

pub fn set_led(led: i64)