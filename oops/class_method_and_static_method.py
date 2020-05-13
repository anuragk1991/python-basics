import datetime

class Employee:
	#class variable
	prof_tax = 200

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def monthlysalary(self):
		#we are using Employee class variable(prof_tax) here not object variable
		return self.salary/12 - Employee.prof_tax

	def __str__(self):
		return 'Employee(First:{}, Last:{}, Salary:{})'.format(self.first, self.last, self.salary)

	@classmethod
	def set_prof_tax(cls, amt):
		cls.prof_tax = amt

	@classmethod
	def fromString(cls, emp_str):
		first, last, salary = emp_str.split('-')
		return cls(first, last, salary)

	@staticmethod
	def is_workday(day):
		'''
		Method to check whether the given day is a working day or not
		@param day: date type object

		'''
		return day.weekday() != 5 and day.weekday != 6


e1 = Employee('Anurag', 'Kumar', 120000)

print('Monthly Salary')
print(e1.monthlysalary()) 

print('Updating prof tax')
Employee.set_prof_tax(300)

print('New Monthly Salary')
print(e1.monthlysalary()) 

date = datetime.date(2018, 5,  15)
print(date)

print('check whether its work day')
print(Employee.is_workday(date))


emp_str = 'Rahul-Kumar-500000'
print('')
print('Create employee object from string seperated by delimiter \'-\'')
e2 = Employee.fromString(emp_str)
print(e2)

print('')
print(e1.__dict__)
print(Employee.__dict__)
