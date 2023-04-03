use crate::robot::brick;
use std::io::Error;
use std::fs::read_dir;


#[allow(dead_code)]
pub struct Motor {
    port: String,
    path: String,
    count_per_rot: i64,
    driver_name: String,
    available_commands: String,
    available_stop_actions: String
}

impl Motor {
    // methods for initializing class
    pub fn attatch(port: &str) -> Motor {
        let path_ret: String = Self::get_sysfs_path(port); // NOTE: need to use the .clone() method to copy the value so we don't get a 'borrow of moved value' error

        Motor {
            port: port.to_string(),
            path: path_ret.clone(),
            count_per_rot: brick::read_int_file(&(path_ret.clone() + "/count_per_rot")), // NOTE: these are file/folder so need a '/' prefix
            driver_name: brick::read_str_file(&(path_ret.clone() + "/driver_name")),
            available_commands: brick::read_str_file(&(path_ret.clone() + "/commands")),
            available_stop_actions: brick::read_str_file(&(path_ret.clone() + "/stop_actions"))
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
    
}