def find_dup_str(val):

	for i in range(len(val)):
		if val [i] == val[i + 1]:
			return val[i]

str_val = "hasbullah"

print(find_dup_str(str_val))