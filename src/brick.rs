use std::fs;
use std::fs::File;
use std::io::prelude::*;

pub fn read_from_file(path: &str) -> String { // read from file path and return as String.
    let buffer: String = fs::read_to_string(path).expect("failed to read file.");
    return buffer;
}

pub fn write_to_file(path: &str, buffer: &[u8]) -> std::io::Result<()> {
    let mut file = File::create(path)?;
    file.write_all(buffer)?;
    Ok(())
}
