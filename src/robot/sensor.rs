#![allow(dead_code)]
use crate::robot::files;
use std::fs::read_dir;

pub struct Sensor {
    pub port: String,
    path:String,
    pub name: String,
    num_values: u8,
    pub unit: String,
    decimals: u64,
    available_modes: String,
}

impl Sensor {
    // methods for initializing class
    pub fn attatch(port: &str) -> Sensor {
        let path_ret: String = Self::get_sysfs_path(port); // NOTE: need to use the .clone() method to copy the value so we don't get a 'borrow of moved value' error

        Sensor {
                port: port.to_string(),
                path: path_ret.clone(),
                name: files::read_str(&(path_ret.clone() + "/driver_name")),
                num_values: files::read_int(&(path_ret.clone() + "/num_values")) as u8,
                unit: files::read_str(&(path_ret.clone() + "/units")),
                decimals: files::read_int(&(path_ret.clone() + "/decimals")) as u64,
                available_modes: files::read_str(&(path_ret.clone() + "/modes"))
            }
    }

    fn get_sysfs_path(port: &str) -> String {
        let paths = read_dir("/sys/class/lego-sensor/").unwrap();

        for path in paths {
            let test_path: String = path.as_ref().unwrap().path().display().to_string() + "/address";
            if files::read_str(&test_path).trim() == port {
                return path.unwrap().path().display().to_string();
            }
        }
        panic!("Could not find any devices on port: {:?}", port) // panic cuz cannot find a device that should be connected
    }
}