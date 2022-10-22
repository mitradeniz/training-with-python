def sesli_harf_echo(str_s, str_v):
	str_s_list = []
	str_v_list = []

	count = 0
	count1 = 0

	for i in str_s:
		str_s_list.append(i)
	for i in str_v:
		str_v_list.append(i)

	for i in range(len(str_v_list)):
		for j in range(len(str_s_list)):
			
			if str_s_list[j] == str_v_list[i]:
				count += 1
				count1 = j
				break
			
	if count == len(str_v_list):
		return count1 - len(str_v_list) + 1
	else:
		return -1

#['A', 'l', 'i', ' ', 't', 'o', 'p', 'u', ' ', 'a', 't'] = str_s
#['t', 'o', 'p'] = str_v

str_s = "Ali topu at."

while True:
	str_val = input("enter a words: ")

	print(sesli_harf_echo(str_s,str_val))