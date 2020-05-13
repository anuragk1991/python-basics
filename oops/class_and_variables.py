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

	def updateproftax(self, amt):
		Employee.prof_tax += amt


e1 = Employee('anurag', 'kumar', 1200000)
e2 = Employee('amit', 'kumar', 900000)

#professional tax only visible in Employee class
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)

e1.prof_tax = 500
e1.updateproftax(e1.prof_tax)

print(e1.monthlysalary())
print(e2.monthlysalary())

#since we set prof_tax in e1, we can see it in e1 instance as well but not in e2
#we can access e1.prof_tax and change it value so that it'll be unique to e1 instance
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)