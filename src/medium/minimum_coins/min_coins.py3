import sys

file = open(sys.argv[1], 'r')

for line in file:
    coin_sum = 0
    total = int(line)
    
    # Greedy solution; depends on certain coin values (e.g. 1,3,5; 1,5,10,25)
    while total >= 5:
        total -= 5
        coin_sum += 1
    while total >= 3:
        total -= 3
        coin_sum += 1
    while total >= 1:
        total -= 1
        coin_sum += 1
    print(coin_sum)
    
file.close()
