# Read our file into a list of lines
with open('test.dat', 'r') as test:
    # Get a single-line header from our file
    header = test.readline()
    with open('output.dat', 'a') as output:
        output.write('Output of the test\n')
    
    for line in test:
        # print(line)
        
        # Split into the part before and after the equals sign
        values = line.split(',')
        # The first word is the name; remove potential whitespace
        load_cell = values[0].strip()
        # The second word is the value, which needs more processing
        time_of_flight = values[1].strip()

        print(f'load cell: {load_cell} and time of flight: {time_of_flight}')

        with open('output.txt', 'a') as output:
            output.write(f'load cell: {load_cell} and time of flight: {time_of_flight}\n')
        
