x = 'global x'

def test():
	y = 'local y'
	print('Inside function')
	print(x, y)


def another():
	print('Inside function which uses local variable of same name')
	x = 'local x'
	print(x)

def outer():
	x = 'outer x'

	def inner():
		nonlocal x
		# x = 'inner x'
		# print(x)
		print('printing outer variable from nested function using nonlocal')
		print(x)

	inner()
	print(x)

outer()

test()

another()

def yy(z):
	z.append('test')
	# z = [] 
	print(z)

names = ['Anurag', 'Amit', 'Alok']
print(names)
yy(names)
print(names)