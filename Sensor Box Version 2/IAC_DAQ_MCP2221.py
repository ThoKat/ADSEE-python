# Just in case the environment variables were not properly set
import os
os.environ["BLINKA_MCP2221"] = "1"
os.environ["BLINKA_MCP2221_RESET_DELAY"] = "-1"

import board
import busio
import time

import adafruit_vl53l0x
from cedargrove_nau7802 import NAU7802

# Load cell
loadCelSensor = NAU7802(board.I2C(), address=0x2a, active_channels=1)

# Time of flight sensor
i2c = busio.I2C(board.SCL, board.SDA)
tofSensor = adafruit_vl53l0x.VL53L0X(i2c)

print("Starting measurements. \n")

# Perform measurements
try:
    while True:
        # Get sensor readings
        loadCellValue = loadCelSensor.read()
        tofValue = tofSensor.range

        # Output sensor data
        print("Load cell: {:.0f}, Distance: {:.0f}".format(loadCellValue, tofValue))
        # print("Load cell: {:.0f}".format(loadCellValue))

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        
        with open('test2.dat', 'a') as test:
            test.write("Load cell: {:.0f}, Distance: {:.0f}".format(loadCellValue, tofValue)", {time_string}\n")
        with open('test3.dat', 'a') as test:
            test.write(f'{loadCellValue},{tofValue}, {time_string}\n')
        
        # Sleep
        time.sleep(1)

# Exit
except KeyboardInterrupt:
    print("\nexiting...\n")
