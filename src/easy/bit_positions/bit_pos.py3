import sys

file = open(sys.argv[1], 'r')

for line in file:
    tokens = line.split(',')
    num = int(tokens[0])
    pos1 = int(tokens[1])
    pos2 = int(tokens[2])
    
    bit_pos1 = 1 << pos1 - 1
    bit_pos2 = 1 << pos2 - 1
    bit1 = num & bit_pos1
    bit2 = num & bit_pos2
    
    if ((bit1 >> pos1 - 1) == (bit2 >> pos2 - 1)):
        print('true')
    else:
        print('false')
        
file.close()
