import sys

file = open(sys.argv[1], 'r')

for line in file:
    for char in line:
        ascii_val = ord(char)
        if ascii_val >= 65 and ascii_val <= 90:
            # ASCII difference between lower and upper case is 32
            print(chr(ascii_val+32), end='')
        else:
            print(char, end='')
    #print('')  # Unnecessary since above prints newline in file
    
file.close()
