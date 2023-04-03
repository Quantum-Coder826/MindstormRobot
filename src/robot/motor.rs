use crate::robot::brick;
use std::io::{Error, Read, ErrorKind};
use std::fs::{read_dir, ReadDir};


pub struct Motor {
    port: String,
    path: String
}
impl Motor {
    // methods for initializing class
    pub fn attatch(port: &str) -> Motor {
        Motor { // TODO: add extra functions for constants
            port: port.to_string(), 
            path: Self::get_sysfs_path(port)
        }
    }

    fn get_sysfs_path(port: &str) -> String {
        let paths = read_dir("/sys/class/tacho-motor/").unwrap();

        for path in paths {
            let test_path: String = path.as_ref().unwrap().path().display().to_string() + "/address";
            if brick::read_str_file(&test_path).trim() == port {
                return path.unwrap().path().display().to_string();
            }
        }
        panic!("Could not find any devices on port: {:?}", port) // panic cuz cannot find a device that should be connected
    }

    // methods for controlling the tachio-motors
    pub fn command(self, command: &str) {
        brick::write_str_file(&(self.path + "command"), command); // TODO: Add error detection for wrong commands
    }
}