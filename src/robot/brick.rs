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

// function for getting information from the battery
pub fn current_battery() -> f64 {
    let current_now_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/current_now");
    let current_now:f64 = current_now_micro as f64 / 1000000 as f64;
    return current_now;
}

pub fn is_LiIon() -> bool {
    if files::read_str("/sys/class/power_supply/lego-ev3-battery/technology").trim() == "Li-ion" {
        return true;
    } else {
        return false;
    }
}

pub fn max_voltage_battery() -> f64{
    let max_voltage_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_max_design");
    let max_voltage:f64 = max_voltage_micro as f64 / 10000000 as f64;
    return max_voltage;
}

pub fn min_voltage_battery() -> f64{
    let min_voltage_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_min_design");
    let min_voltage:f64 = min_voltage_micro as f64 / 10000000 as f64;
    return min_voltage;
}

pub fn voltage_battery() -> f64 {
    let voltage_now_micro: i64 = files::read_int("/sys/class/power_supply/lego-ev3-battery/voltage_now");
    let voltage_now:f64 = voltage_now_micro as f64 / 1000000 as f64;
    return voltage_now;
}