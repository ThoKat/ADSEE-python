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

dev = False              # Development mode
usbPort = "Com5"      # Your USB port, obtain using port_scan()

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
    ###YOUR CODE HERE###
    with open('test.dat', 'a') as test:
        test.write('Load Cell, Time of Flight\n')
    
    while running:
        # Delay 1 second
        while currentTime + 1 > time.time():
            pass
        currentTime = time.time()
        line = development_data()[:-2].decode('utf-8')
        print(line)
        
        ####################
        ###YOUR CODE HERE###
        ####################

        line1 = line.replace('load_cell ','')
        lineOutput = line1.replace(' time_of_flight',',')

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)

        with open('test.dat', 'a') as test:
            test.write(f'{lineOutput}, {time_string}\n')


else:
    ###YOUR CODE HERE###
    with open('testReal.dat', 'a') as test:
        test.write('load_cell, time_of_flight, time\n')
        test.write('1365.3 + 0 > 1365.3 + 2625.9\n') #3991.2
    
    while running:
        line = ser.readline()[:-2].decode('utf-8')
        print(line)
        
        ####################
        ###YOUR CODE HERE###
        ####################

        line1 = line.replace('load_cell: ','')
        lineOutput = line1.replace(' time_of_flight:',',')

        lineSplit = lineOutput.split(',')

        a = -0.0058 #-0.022666378
        b = 4912.2  #347.2132836 

        try:
            print(lineSplit[0])
            force = float(lineSplit[0])*a + b
            print('Force: ',force)
        except:
            print("N")
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)

        #print(time_string)
        
        with open('testReal.dat', 'a') as test:
            test.write(f'{lineOutput}, {time_string}\n')
            
        try:
            ValueCall = int(lineSplit[0])
            with open('testCal1.dat', 'a') as test:
                test.write(f'{ValueCall}\n')
        except:
            print("N")
