from math import *

def sum_digit(num):

	result = 0

	while num > 0:
		result += num % 10
		num = floor(num / 10)

	return result

while True:
	num = int(input("Enter a numb: "))

	print(sum_digit(num))