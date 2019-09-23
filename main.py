from machine import Pin, I2C
from AS7265X import AS7265X
import time

sensor_type = "None"

try:
    i2c = I2C(0, I2C.MASTER, pins=('P22', 'P21'))
    sensor = AS7265X(i2c=i2c) # create and use non-default PIN assignments (P22=SDA, P21=SCL)
    sensor_type = sensor.get_device_type()
    print("Sensor type: {}".format(sensor_type))
    print("Wavelengths: {}".format(sensor.get_wavelengths()))
    time.sleep(1)
except Exception as error:
    print(error)
    pass

while True:
    calibrated_values = []
    try:
        sensor.take_measurements()
        calibrated_values = sensor.get_all_values(calibrated=True)
        print(calibrated_values)

    except Exception as error:
        print(error)

    time.sleep(5.0)
