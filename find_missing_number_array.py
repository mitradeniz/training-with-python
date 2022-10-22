def sort(arr):

	tmp = 0

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] < arr[j]:
				tmp = arr[i]
				arr[i] = arr[j]
				arr[j] = tmp
	return arr

def find_missing(arrs):
	arr = sort(arrs)

	for i in range(1, len(arr) + 1):
		if i != arr[i - 1]:
			return i

arr = [1,2,3,5]

print(sort(arr))
print(find_missing(arr))