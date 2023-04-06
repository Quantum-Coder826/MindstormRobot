#![allow(dead_code)]
use crate::robot::files;
use std::fs::read_dir;

#[derive(Debug)]
pub enum SensorReturn<I, F> {
    Int(I),
    Float(F)
}
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
                available_modes: files::read_str(&(path_ret.clone() + "/modes")),
                num_values: files::read_int(&(path_ret.clone() + "/num_values")) as u8, // all field from here change when fn set_mode is called
                unit: files::read_str(&(path_ret.clone() + "/units")),
                decimals: files::read_int(&(path_ret.clone() + "/decimals")) as u64
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

    // methods for interacting with sensors
    pub fn set_mode(&mut self, mode: &str) {
        if !self.available_modes.trim().contains(mode) {
            panic!("Mode: {:?} is not a valid, valid modes are: {:?}", mode, self.available_modes);
        }
        files::write_str(&(self.path.clone() + "/mode"), mode);

        self.num_values = files::read_int(&(self.path.clone() + "/num_values")) as u8;
        self.unit = files::read_str(&(self.path.clone() + "/units"));
        self.decimals = files::read_int(&(self.path.clone() + "/decimals")) as u64;
    }


    pub fn get_value(&self, value: u8) -> SensorReturn<i64, f64>{
        let data_raw: i64 = files::read_int(&(self.path.clone() + "/value" + &value.to_string()));
        if self.decimals == 1 {
            let mut i: u64 = 0;
            let mut data:f64 = data_raw as f64;
            while i < self.decimals {
                data = data / 10.0;
                i = i + 1;
            }
            return SensorReturn::Float(data);
        } else {
            return SensorReturn::Int(data_raw);
        }
    }
}