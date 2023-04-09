# sensor.rs
All methods in these files could theoreicaly read data form all available sensors for the lego mindstorms. It is recocmende to check [this](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html) page on the ev3dev site to understand where a sensor sends it's data, how to read it and wich available mode there are. For more info on all aspects of a sensor check [this](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html#sysfs) page.

## the mehods
### ```attatch(port: &str) -> Sensor```
This metod is reqired to use a sensor the `port` paramater should look like `ev3-ports:in<N>` where N is the number corresponding to the port a sensor is connected to.
> **_NOTE:_** when attaching a sensor the code sould look like this: ```let mut sensor = Sensor.attatch("ev3-ports:in1")``` the returned Sensor struct **must** be mutale othewise the `set_mode` method will not work.

### ```set_mode(&mut self, mode: &str)```
Sets the mode of a sensor to the mode specifide in the `mode` parameter. Check [Appendix A: Sensor Data](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html) on the ev3dev site and find the sensor that is being used. All information on which modes are available and what they do is listed there for basicly all supported sensors.

### ```get_value(&self, value: u8) -> SensorReturn<i64, f64>```
This method does some wired stuff. It reads a value form the sensor which is specifed as a numer in the `value` parameter. See the [Appendix A: Sensor Data](https://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html) to figue out wich values you can read and what data they contain. And becouse the sensor can ether retun a integer or a float the enum SensorRetun is used. This means reading data form a sensor should look like this:
``` rust
let value: i64 = match sensor.get_value(0) {
    SensorReturn::Int(value) => value,
    SensorReturn::Float(_) => 0
}
```
this snippet will only retun a integer valu otherwilse a zero for a float it should look like:
``` rust
let value: i64 = match sensor.get_value(0) {
    SensorReturn::Int(_) => 0,
    SensorReturn::Float(value) => value
}
```
Never expect the sensor to return interger and float values, the underlying sysfs files do not allow that behaviour.