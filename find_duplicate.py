def find_duplicate(arr):
	
	count = 0
	control = 0

	for i in range(count+1, len(arr)+1):
		tmp = arr[count]
		for i in arr:
			if i == tmp:
				control += 1
		if control == 1:
			break
		else:
			control = 0
		count += 1
	return tmp

arr = [1,1,2,2,3,3,4,4,5,5,6,7,7]
print(find_duplicate(arr))
