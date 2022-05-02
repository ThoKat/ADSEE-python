# Thomas van Wijk, 26-04-2022 11:05
# -*- coding: utf-8 -*-
"""
This program is used to load the data from the USB serial.
Whenever the serial port receives data, it will be placed in the "line" variable. From here, it needs to be parsed and saved.
 
You can enable a "development" mode which will feed fake data by setting dev = True
"""

import serial
import time
from IAC_helper import port_scan, development_data

dev = False             # Development mode
usbPort = "Com5"        # Your USB port, obtain using port_scan()
force = 0
distance = 0

try:
    if not dev:
        ser = serial.Serial(usbPort, 9600)
    if dev:
        print('Ports: ',port_scan())
    running = True
    print("Serial initialized succesfully!")
except:
    print("Issue with serial! Aborting...")


if dev:
    currentTime = time.time()
    with open('test.dat', 'a') as test:
        test.write('Load Cell, Time of Flight\n')
    
    while running:
        # Delay 1 second
        while currentTime + 1 > time.time():
            pass
        currentTime = time.time()
        line = development_data()[:-2].decode('utf-8')
        print(line)

        line1 = line.replace('load_cell ','')
        lineOutput = line1.replace(' time_of_flight',',')

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)

        with open('test.dat', 'a') as test:
            test.write(f'{lineOutput}, {time_string}\n')


else:
    with open('testReal.dat', 'a') as test:
        test.write('load_cell, time_of_flight, time\n')
    
    with open('testReal2.dat', 'a') as test:
        test.write('Load Cell (N), Distance, Time\n')
    
    with open('testCal1.dat', 'a') as test:
        test.write('New calibration data\n')
    
    while running:
        line = ser.readline()[:-2].decode('utf-8')
        print(line)

        line1 = line.replace('load_cell: ','')
        lineOutput = line1.replace(' time_of_flight:',',')

        lineSplit = lineOutput.split(',')

        a = -0.0058
        b = 4912.2

        try:
            print(lineSplit[0])
            gram = float(lineSplit[0])*a + b
            print('Grams: ',gram)
            kilo = gram/1000
            force = kilo*9.81
            print('Force: ',force)
            distance = lineSplit[1]
            print('Distance: ',distance)
        except:
            pass
        
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)

        
        with open('testReal.dat', 'a') as test:
            test.write(f'{lineOutput}, {time_string}\n')
            
        with open('testReal2.dat', 'a') as test:
            test.write(f'{force}, {distance}, {time_string}\n')
            
        try:
            ValueCall = int(lineSplit[0])
            with open('testCal1.dat', 'a') as test:
                test.write(f'{ValueCall}\n')
        except:
            pass
