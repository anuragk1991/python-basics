class Employee:
	prof_tax = 200

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def fullname(self):
		return f'{self.first} {self.last}'

	def __str__(self):
		return f'Employee(First: {self.first}, Last: {self.last}, Salary: {self.salary})'

class Developer(Employee):
	prof_tax = 300

	def __init__(self, first, last, salary, lang):
		super().__init__(first, last, salary)
		self.lang = lang

	def get_language(self):
		return self.lang

	def __str__(self):
		return f'Developer(First: {self.first}, Last: {self.last}, Salary: {self.salary}, Language: {self.lang})'


class Manager(Employee):
	prof_tax = 500

	def __init__(self, first, last, salary, emplist = None):
		super().__init__(first, last, salary)

		if emplist is None:
			self.emplist = []
		else:
			self.emplist = emplist

	def manages(self):
		for emp in self.emplist:
			print(emp.fullname())

	def add_emp(self, emp):
		if emp not in self.emplist:
			self.emplist.append(emp)

	def add(self, *args):
		for emp in args:
			self.add_emp(emp)

	def remove_emp(self, emp):
		if emp in self.emplist:
			self.emplist.remove(emp)

	def remove(self, *args):
		for emp in args:
			self.remove_emp(emp)

	def __str__(self):
		return f'Manager(First: {self.first}, Last: {self.last}, Salary: {self.salary}, Manages: {", ".join([emp.fullname() for emp in self.emplist])})'

e1 = Employee('Riju', 'Choudhuri', 1200000)
dev1 = Developer('Anurag', 'Kumar', 12000000, 'PHP')
manager = Manager('Sandeep', 'Singh', 4000000)

manager.add(e1, dev1)

print(e1)
print(dev1)
print(manager)

manager.remove(e1)

print(manager)