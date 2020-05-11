test = 'Test Variable'

def find_index(search, value):
	for key, val in enumerate(search):
		if val == value:
			return key

	return -1

