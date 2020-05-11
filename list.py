courses = ['Science', 'Art', 'Engg', 'CompSci', 'Physics']

# courses.sort()
print("Print list")
print(courses)

print('Adding items in list')
print("")

print('Append method takes one parameter to insert an element at the end of the list -- append Maths at the end of the list')
courses.append('Maths')
print(courses)
print("")
print('Insert method takes two parameter to insert an element at given index of the list -- insert Java at the 1 index of the list')
courses.insert(1,'Java')

print(courses)

print("")
print("Sorting in list")
print("")
print("Sorted function returns sorted list but do not change the list itself")
print(sorted(courses))
print('Original list')
print(courses)
print("Sort method of list class returns None but sorts the list itself")
courses.sort()
print(courses)
print("")
courses_2 = ['MP', 'ECE', 'Chemistry']
print('Another list')
print(courses_2)

print("")
print('Extend method merge another list into the list. It takes exactly one argument. Note: It will create duplicate elements if there same items in two lists')
courses.extend(courses)
print(courses)

print("")

print('Removing item in list')
courses.remove('Art')
print(courses)

print('')
print('Looping through list')
print('')

for val in courses:
	print(val)

print('')
print('For index value pair use enumerate function')
print('')

for key, val in enumerate(courses):
	print("Course as index {}: {}".format(key, val))	


print('')
print('Start index from 1, pass start=1 in enumerate function')
print('')

for key, val in enumerate(courses, start=1):
	print("Course as index {}: {}".format(key, val))	


print('')
print('Join a list i.e convert in string using str.join(list)')
print('')
print(', '.join(courses))
print(courses)
