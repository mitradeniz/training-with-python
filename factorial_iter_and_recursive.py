def fact_iter(num):
	result = 1
	for i in range(1, num + 1):
		result *= i
	return result

def fact_recursive(num):
	if num == 1:
		return num
	else:
		return num * fact_recursive(num - 1)



print(fact_recursive(5))		
