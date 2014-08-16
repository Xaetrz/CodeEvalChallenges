import sys

file = open(sys.argv[1], 'r')

for line in file:
	nums = line.split(" ")
	div1 = int(nums[0])
	div2 = int(nums[1])
	
	for n in range(1, int(nums[2]) + 1):
		if n % div1 == 0:
			if n % div2  == 0:
				print('FB', end=" ")
			else:
				print('F', end=" ")
		elif n % div2  == 0:
			print('B', end=" ")
		else:
			print(n, end=" ")
	print("")
	
file.close()
