def rec_pow(num, x):

	if x == 1:
		return num

	return num * rec_pow(num, x - 1)


a = 2

print(rec_pow(2,6))