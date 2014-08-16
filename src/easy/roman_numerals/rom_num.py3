import sys
import math

def print_roman(digit, low_symb, mid_symb, hi_symb):
	# Each digit in a decimal number operate by same rules for 
	# conversion to roman numerals related to placement of numerals
	if digit <= 3:
		for i in range(digit):
			print(low_symb, end="")
	elif digit == 4:
		print(low_symb + mid_symb, end="")
	elif digit <= 8:
		print(mid_symb, end="")
		for i in range(digit - 5):
			print(low_symb, end="")
	else:
		print(low_symb + hi_symb, end="")

		
file = open(sys.argv[1], 'r')

for num_str in file:
	num = int(num_str)
	# range = [1...3999]
	thousands = math.floor(num/1000) % 10
	hundreds = math.floor(num/100) % 10
	tens = math.floor(num/10) % 10
	ones = num % 10
	
	# Thousands do not go higher than 3
	for t in range(thousands):
		print("M", end="")
	
	print_roman(hundreds, "C", "D", "M")
	print_roman(tens, "X", "L", "C")
	print_roman(ones, "I", "V", "X")
	print("")
