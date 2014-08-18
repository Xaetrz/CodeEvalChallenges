import sys

file = open(sys.argv[1], 'r')

for line in file:
    nums = line.split(',')
    # Important: Initialize to num that exists in the list
    max_sum = int(nums[0]) 
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):  
            curr_sum += int(nums[j])
            if max_sum < curr_sum:
                max_sum = curr_sum
                
    print(max_sum)