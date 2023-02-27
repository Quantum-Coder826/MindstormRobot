use std::fs;
use std::fs::File;
use std::io::prelude::*;

// function for interacting with sysfs, and comverting strings to int.
pub fn read_from_file(path: &str) -> String { // read from file path and return as String.
    let mut buffer: String = fs::read_to_string(path).expect("failed to read file.");
    buffer.pop(); // remove newline at end of string
    return buffer;
}

pub fn write_to_file(path: &str, buffer: &[u8]) -> std::io::Result<()> { // write string to a file path
    let mut file:File = File::create(path)?;
    file.write_all(buffer)?;
    Ok(())
}

// functions for interacting with the brick hardware.
pub fn battery_current() -> f64 { // retun the current draw on the battery in amps
    let microamps: f64 = read_from_file("/sys/class/power_supply/lego-ev3-battery/current_now").parse().unwrap();
    let amps: f64 = microamps / 1000000.0;
    return amps;
}

pub fn battery_is_LiIon() -> bool { // returns true if a Li-ion battery is installed
    let tech: String = read_from_file("/sys/class/power_supply/lego-ev3-battery/technology");
    if tech == "Li-ion" {
        return true;
    } else {
        return false;
    };
}

pub fn battery_max_voltage() -> f64 { // retun the nominal "full" battery voltage in volts
    let microvolts: f64 = read_from_file("/sys/class/power_supply/lego-ev3-battery/voltage_max_design").parse().unwrap();
    let volts: f64 = microvolts / 1000000.0;
    return volts;
}

pub fn battery_min_voltage() -> f64 { // retun the nominal "empty" battery voltage in volts
    let microvolts: f64 = read_from_file("/sys/class/power_supply/lego-ev3-battery/voltage_min_design").parse().unwrap();
    let volts: f64 = microvolts / 1000000.0;
    return volts;
}

pub fn battery_voltage() -> f64 { // retun the current draw on the battery in amps
    let microvolts: f64 = read_from_file("/sys/class/power_supply/lego-ev3-battery/voltage_now").parse().unwrap();
    let volts: f64 = microvolts / 1000000.0;
    return volts;
}