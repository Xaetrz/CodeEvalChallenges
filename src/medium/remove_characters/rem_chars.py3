import sys

def contains_char(char, chars_list):
    for x in chars_list:
        if char == x:
            return True
    return False

    
file = open(sys.argv[1], 'r')

for line in file:
    tokens = line.split(',')
    rem_chars = list(tokens[1].strip())
    
    for char in tokens[0]:
        if not contains_char(char, rem_chars):
            print(char, end='')
    print('')                

file.close()
