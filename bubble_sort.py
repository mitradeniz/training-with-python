def sort(arr):
	tmp = 0

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] < arr[j]:
				tmp = arr[j]
				arr[j] = arr[i]
				arr[i] = tmp
	return arr			


arr = [5,2,3,5,7,4,3,2,4,5,6,4,2,32]

print(sort(arr))