# Thomas van Wijk, 26-04-2022 12:12
with open('Real Test Readout.dat', 'r') as test:
    header = test.readline()
    with open('outputForce.txt', 'a') as output:
        output.write('Output of the test\n')
    
    for line in test:
        values = line.split(',')
        force = values[0].strip()
        distance = values[1].strip()
        time = values[2].strip()
        try:
            print(f'Force: {force}, distance: {distance} and time: {time}')
            forceOut = float(force) - 110.695228713
            
            with open('outputForce.txt', 'a') as output:
                output.write(f'{forceOut}\n')
        except:
            pass
        
