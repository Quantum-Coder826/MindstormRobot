#![allow(dead_code)]
use crate::robot::files;
use std::fs::read_dir;

pub struct Motor {
    port: String,
    path: String,
    count_per_rot: i64,
    pub name: String,
    available_commands: String,
    available_stop_actions: String
}

impl Motor {
    // methods for initializing class
    pub fn attatch(port: &str) -> Motor {
        let path_ret: String = Self::get_sysfs_path(port); // NOTE: need to use the .clone() method to copy the value so we don't get a 'borrow of moved value' error
        (&(path_ret.clone() + "/command"), "reset");

        Motor {
            port: port.to_string(),
            path: path_ret.clone(),
            count_per_rot: files::read_int(&(path_ret.clone() + "/count_per_rot")), // NOTE: these are file/folder so need a '/' prefix
            name: files::read_str(&(path_ret.clone() + "/driver_name")),
            available_commands: files::read_str(&(path_ret.clone() + "/commands")),
            available_stop_actions: files::read_str(&(path_ret.clone() + "/stop_actions"))
        }
    }

    fn get_sysfs_path(port: &str) -> String {
        let paths = read_dir("/sys/class/tacho-motor/").unwrap();

        for path in paths {
            let test_path: String = path.as_ref().unwrap().path().display().to_string() + "/address";
            if files::read_str(&test_path).trim() == port {
                return path.unwrap().path().display().to_string();
            }
        }
        panic!("Could not find any devices on port: {:?}", port) // panic cuz cannot find a device that should be connected
    }

    // methods to send commands to tacho motors
    pub fn run_forever(self, speed_sp: i16) {
        files::write_int(&(self.path.clone() + "/speed_sp"), &(speed_sp as i64));
        files::write_str(&(self.path.clone() + "/command"), "run-forever");
        return;
    }

    pub fn run_abs_pos(self, angle_sp: i16, speed_sp: i16) {
        files::write_int(&(self.path.clone() + "/speed_sp"), &(speed_sp as i64));
        files::write_int(&(self.path.clone() + "/position_sp"), &(angle_sp as i64));
        files::write_str(&(self.path.clone() + "/command"), "run-to-abs-pos");
        return;
    }

    pub fn run_rel_pos(self, angle_sp: i16, speed_sp: i16) {
        files::write_int(&(self.path.clone() + "/speed_sp"), &(speed_sp as i64));
        files::write_int(&(self.path.clone() + "/position_sp"), &(angle_sp as i64));
        files::write_str(&(self.path.clone() + "/command"), "run-to-rel-pos");
        return;
    }
    
    pub fn run_timed(self, time_sp: u64, speed_sp: i16) {
        files::write_int(&(self.path.clone() + "/time_sp"), &(time_sp as i64));
        files::write_int(&(self.path.clone() + "/speed_sp"), &(speed_sp as i64));
        files::write_str(&(self.path.clone() + "/command"), "run-timed");
        return;
    }

    pub fn run_duty(self, duty_sp: i8) {
    if duty_sp < -100 || duty_sp > 100 { // var uty_sp must be in range -100 to 100
        panic!("duty_sp is: {:?} must be in rage -100 to 100", duty_sp);
    } else {
        files::write_int(&(self.path.clone() + "/duty_cycle_sp"), &(duty_sp as i64));
        files::write_str(&(self.path.clone() + "/command"), "run-direct");
        return;
    }}

    pub fn stop(self) {
        files::write_str(&(self.path.clone() + "/command"), "stop");
        return;
    }

    pub fn reset(self) {
        files::write_str(&(self.path.clone() + "/command"), "reset");
        return;
    }
    
}