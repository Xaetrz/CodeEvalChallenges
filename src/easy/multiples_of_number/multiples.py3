import sys

file = open(sys.argv[1], 'r')

for line in file:
    nums = line.split(',')
    multi = int(nums[1])
    while (multi < int(nums[0])):
        multi += int(nums[1])
    print(multi)
	
file.close()
