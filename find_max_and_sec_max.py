def find_max_and_sec_max(arr):
	max_num = arr[0]
	max_sec_num = arr[0]

	for i in arr:
		if i > max_num:
			max_num = i;

	arr.remove(max_num)

	for i in arr:
		if i > max_sec_num:
			max_sec_num = i;
	return max_num, max_sec_num

arr = [12,4,3,64,67,3,2,6,8,5,2,4,65,23,12,650,75,32,5,44,12,765,0,-15,-3]

print(find_max_and_sec_max(arr))

