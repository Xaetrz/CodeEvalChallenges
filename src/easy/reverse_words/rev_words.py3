import sys

file = open(sys.argv[1], 'r')

for line in file:
	line = line.strip() # Remove new line
	words = line.split()
	for i in range(len(words)-1, -1, -1):
		print(words[i], end=" ")
	print("")
