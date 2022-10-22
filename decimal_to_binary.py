from math import *

def dec_to_bin(num):
	result_arr = []

	while num > 0:
		result_arr.append(num % 2)
		num = floor(num / 2)
	
	return result_arr



print(dec_to_bin(6))
