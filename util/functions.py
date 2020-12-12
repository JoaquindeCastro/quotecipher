def get_unique_key(lst, number=None):
	if number == None:
		return get_unique_key(lst, number=1)
	elif number in lst:
		number+=1
		return get_unique_key(lst, number)
	else:
		return number

def get_key(dictionary, value):
	for key, val in dictionary.items():
		if val == value:
			return key