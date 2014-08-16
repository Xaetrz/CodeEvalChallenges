import sys
import math
	
def is_palindrome(num):
	num_str = str(num)
	for i in range(int(num_str.__len__()/2)):
		if num_str[i] != num_str[num_str.__len__() - i - 1]:
			return False
	return True
	
def is_prime(num):
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True
	
for i in range(1000, 1, -1):
	if is_palindrome(i) and is_prime(i):
		print(i)
		break