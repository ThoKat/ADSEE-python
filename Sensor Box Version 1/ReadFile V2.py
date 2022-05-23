# Thomas van Wijk, 26-04-2022 12:12
with open('testReal2.dat', 'r') as test:
    header = test.readline()
    with open('outputReal.txt', 'a') as output:
        output.write('Output of the test\n')
    
    for line in test:
        values = line.split(',')
        force = values[0].strip()
        distance = values[1].strip()
        time = values[2].strip()

        print(f'Force: {force}, distance: {distance} and time: {time}')

        with open('outputReal.txt', 'a') as output:
            output.write(f'load cell: {load_cell} and time of flight: {time_of_flight}\n')
        
