# Thomas van Wijk, 26-04-2022 12:12
with open('test.dat', 'r') as test:
    header = test.readline()
    with open('output.txt', 'a') as output:
        output.write('Output of the test\n')
    
    for line in test:
        # print(line)
        values = line.split(',')
        load_cell = values[0].strip()
        time_of_flight = values[1].strip()

        print(f'load cell: {load_cell} and time of flight: {time_of_flight}')

        with open('output.txt', 'a') as output:
            output.write(f'load cell: {load_cell} and time of flight: {time_of_flight}\n')
        
