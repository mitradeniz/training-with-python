def str_pal(val):

	val_list = []

	for i in val:
		val_list.append(i)


	i = len(val) - 1

	pal_list = []

	for j in range(len(val)):
		pal_list.append(val_list[i])
		i -= 1

	pal_str = ""

	for x in pal_list:
		pal_str += x

	return pal_str


str_val = "murder king"

print(str_pal(str_val))