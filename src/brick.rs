use std::fs::File;
use std::io::{BufReader, Read};

// functions for handeling file reads
pub fn file_read_string(path: &str) -> String {
    let file: File = File::open(path).expect("Faild to read the file");
    let mut file_buff = BufReader::new(file);

    let mut data:String = String::new();
    file_buff.read_to_string(&mut data).expect("Faild to read string");
    return data;
}

pub fn file_read_int(path: &str) -> i64 {
    let file: File = File::open(path).expect("Faild to read the file");
    let mut file_buff = BufReader::new(file);

    let mut raw_data:String = String::new();
    file_buff.read_to_string(&mut raw_data).expect("Faild to read int");

    let data: i64 = raw_data.trim().parse::<i64>().unwrap(); // do not forget to trim the string when type casting
    return data;
}