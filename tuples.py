tuple = (1,2,5,6)
print('Tuple')
print(tuple)
print('')

print('We can access value at particular index same as we do in list tuple[2]')
print(tuple[2])

print('')
print('We cannot modify the values of tuple because tuple is immutable, if we try to modify value at any index it will result in item assignment Error')
tuple[2] = 4

tuple[4] = 9