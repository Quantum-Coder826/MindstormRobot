use crate::robot::brick;
use std::io::{Error, Read};
use std::fs::{read_dir, ReadDir};


pub struct Motor {
    port: String,
    path: String
}

impl Motor {
    pub fn attatch(port: &str) -> Self {
        Motor { 
            port: port.to_string(), 
            path: get_sysfs_path(port)
        }}
    }

    fn get_sysfs_path(port: &str) -> String {
        let paths = read_dir("/sys/class/tacho-motor/").unwrap();
        
        for path in paths {
            let test_path = path.unwrap().path().display().to_string() + "address";
            if brick::file_read_string(&test_path) == port {
                return path.unwrap().path().display().to_string();
            }
        }
        panic!("Could not find any devices on port: {:?}", port) // panic cuz cannot find a device that should be connected

    }
