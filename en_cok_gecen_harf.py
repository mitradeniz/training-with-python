def en_cok_gecen_harf(val_strs):

	val_str = []

	for i in val_strs:
		val_str.append(i)

	tmp = []

	count = 0

	for i in range(len(val_str)):
		for j in range(len(val_str)):
			if val_str[i] > val_str[j]:
				tmp = val_str[i]
				val_str[i] = val_str[j]
				val_str[j] = tmp
	i = 0

	list_sorted = []

	while i != len(val_str):
		for j in range(len(val_str)):
			if val_str[i] == val_str[j]:
				count += 1

		list_sorted.append(val_str[i])
		list_sorted.append(count)
		i += count
		count = 0
	return list_sorted


def get_more_char(arr_chr_input):
	arr_chr = en_cok_gecen_harf(arr_chr_input)

	i = 1
	ind = 0
	max_val = 0

	while i <= len(arr_chr):
		if int(arr_chr[i]) > max_val:
			max_val = arr_chr[i]
		i += 2

	for x in arr_chr:
		if arr_chr[ind] == max_val:
			return arr_chr[ind - 1]
		else:
			ind += 1


val_strs = "fdshşglskdjflgkjfaldjglsdjlgkjsdflkjglşsdkfj"



#print(en_cok_gecen_harf(val_str))

print(en_cok_gecen_harf(val_strs))
print("\n\n")
print(get_more_char(val_strs))