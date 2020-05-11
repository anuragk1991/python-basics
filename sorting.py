li = [3,5,5,3,2,4,6,8,4,9]

print('sorted function creates new list and doesn\'t change the original list')

s_li = sorted(li)
print('Original List')
print(li)
print('Sorted List')
print(s_li)

print('sort() method on list sorts the list itself and returns None')


print('Sort in desc order by passing reverse=True parameter in sorted function')



d_li = sorted(li, reverse=True)
print(d_li)

print('')
print('Sorting dictionary')

print('')
print('dict')

dict = {'Anurag', 'Amit', 'Alok', 'Riju', 'Ajay'}
print(dict)
print('')
print('Sorted Dict')
print(sorted(dict, reverse=True))


print('')
print('Sorting class objects')


class Employee:
	name = None
	age = None
	role = None
	def __init__(self, name, age, role):
		self.name = name
		self.age = age
		self.role = role

	def __repr__(self):
		return 'Employee({emp.name}, {emp.age}, {emp.role})'.format(emp = self)
employees = []
employees.append(Employee('Anurag', 29, 'Developer'))
employees.append(Employee('Amit', 31, 'QA'))
employees.append(Employee('Alok', 38, 'Manager'))


from operator import attrgetter

s_emp = sorted(employees, key=attrgetter('age'), reverse=True)
print(s_emp)

roles = [emp.role for emp in employees]
print(roles)