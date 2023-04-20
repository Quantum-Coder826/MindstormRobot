use std::io::Error;
use std::fs::File;
use std::fs::OpenOptions;
use std::io::{BufReader, Read, Write};

// functions for handeling file reads
pub fn read_str(path: &str) -> String {
    let file_result: Result<File, Error> = File::open(path);
    let file:File = match file_result {
        Ok(file) => file,
        Err(error) => panic!("Faild to read file: {:?}, Error: {:?}", path, error)
    };
    let mut file_buff:BufReader<File> = BufReader::new(file);

    let mut data:String = String::new();
    file_buff.read_to_string(&mut data).expect("Faild to read string");
    return data;
}

pub fn read_int(path: &str) -> i64 {
    let file_result: Result<File, Error> = File::open(path);
    let file:File = match file_result {
        Ok(file) => file,
        Err(error) => panic!("Faild to read file: {:?}, Error: {:?}", path, error)
    };
    let mut file_buff = BufReader::new(file);

    let mut raw_data:String = String::new();
    file_buff.read_to_string(&mut raw_data).expect("Faild to read int");

    let data: i64 = raw_data.trim().parse::<i64>().unwrap(); // not to self: do not forget to trim the string when type casting
    return data;
}

// function for handeling binary file read
pub fn read_bytes(path: &str, buf_size: usize) -> Vec<u8> {
    let file_result: Result<File, Error> = File::open(path);
    let file:File = match  file_result {
        Ok(file) => file,
        Err(error) => panic!("Faild to read file: {:?}, Error: {:?}", path, error)
    };
    let mut file_buff: BufReader<File> = BufReader::new(file);
    let mut bytes: Vec<u8> = vec![0; buf_size];
    let _ = file_buff.read_exact(&mut bytes);
    return bytes;
}

// functions for handeling file writes
pub fn write_str(path: &str, data: &str) {
    let file_result:Result<File, Error> = OpenOptions::new().write(true).open(path);
    let mut file:File = match file_result {
        Ok(file) => file,
        Err(error) => panic!("Faild to write file: {:?} data: {:?} Error: {:?}", path, data, error)
    };
    file.write_all(format!("{}", data).as_bytes()).unwrap();
}

pub fn write_int(path: &str, data: &i64) {
    let file_result:Result<File, Error> = OpenOptions::new().write(true).open(path);
    let mut file:File = match file_result {
        Ok(file) => file,
        Err(error) => panic!("Faild to write file: {:?} data: {:?} Error: {:?}", path, data, error)
    };
    file.write_all(format!("{}", data).as_bytes()).unwrap();
}
