from module import find_index as fi

names = ['Anurag', 'Amit', 'Riju']

index = fi(names, 'Amit')

if index != -1:
	print('Value found at index {}'.format(index))
else:
	print('Value not found!')
# print(module.test)