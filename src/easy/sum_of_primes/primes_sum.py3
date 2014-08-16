import sys
import math

def is_prime(num):
	for i in range(2, int(math.sqrt(num)+1)):
		if num % i == 0:
			return False
	return True

sum = 0
num_primes = 0
iter = 2
while num_primes < 1000:
	if is_prime(iter):
		sum += iter
		num_primes += 1
	iter += 1
print(sum)
