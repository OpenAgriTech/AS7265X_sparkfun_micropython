# AS7265X_sparkfun_micropython
MicroPython driver for the AS7265X 18-channels spectral sensor

This is a python library for the AS7265X 18-channels spectral sensor designed to operate with Pycom's boards. It is based on SparkFun_AS7265x_Arduino_Library : https://github.com/sparkfun/SparkFun_AS7265x_Arduino_Library.


Original library contact : Facebook https://www.facebook.com/KueriotUnited/ or https://www.facebook.com/Kanoon.Charoentananuwat


The library has been modified with minor style changes and naming of the functions. A function for providing the wavelengths has been provided.
A sample program for the LoPy is provided using non-default I2C PIN assignments (P22=SDA, P21=SCL) (avoid using the LED pin on expansion boards).
