def is_prime(num):
	# True ise asal
	if num == 1:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False

	return True


while True:

	val = int(input("Enter a number pls: "))

	print(is_prime(val))