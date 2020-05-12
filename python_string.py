# simple srtring
msg = "Hello World"

print("Print complete string")
print(msg)
print(msg[:]) # same as print(msg)

#[start_index:end_index:step] - start_index is inclusive and end_index is exclusive
print("Print string from 0 to 4")
print(msg[0:5])

print("Print string from 0 to 4 with step 2")
print(msg[0:5:2])


print("")
print("")

print("================================================================")
print("=                                                              =")
print("=                      String Formating                        =")
print("=                                                              =")
print("================================================================")

print("")

user = {'name': 'Anurag', 'age': 29}

print("Formating string with numbered parameter - below example with two parameters")
sentence = 'Hello {0}, Your age is {1}'.format(user['name'], user['age'])
print(sentence)

print("Formating string with numbered parameter - below example with dictionary  parameter")
sentence = "Hello {0[name]}, Your age is {0[age]}".format(user)
print(sentence)

print("Formating string with keyword arguments (namme and age)")
sentence = "Hello {name}, Your age is {age}".format(name=user['name'], age=user['age'])
print(sentence)

print("Formating string with keyword arguments (namme and age) using unpacking dictionary")
sentence = "Hello {name}, Your age is {age:03}".format(**user)
print(sentence)

newStr = f"{user['name']} is a Software Developer of age: {user['age']}"
print(f"{user['name']} is a Software Developer of age: {user['age']}")
