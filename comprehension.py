nums = [1,2,3,4,5,6,7,8,9]
print(nums)

print('List comprehension')
my_list = [n for n in nums]
print(my_list)
print('')

print('Create list from another list (n*n) using list map and lambda function')
my_list = map(lambda n: n*n, nums)
print(my_list)
print('')

print('Create list from another list (n*n)  using list comprehension')
my_list = [n*n for n in nums]
print(my_list)
print('')

print('Create list of even numbers another list using list filter and lambda function')
my_list = filter(lambda n: n%2==0, nums)
print(my_list)
print('')

print('Create list of even numbers from another list using list comprehension')
my_list = [n for n in nums if n%2 == 0]
print(my_list)
print('')

print('Create a list of tuples(char, digit) from two array of same length using list comprehension')

letters = 'abcd'
numbers = '1234'

my_list = [(char, digit) for char in letters for digit in numbers]
print(my_list)


names = ['Bruce', 'Clark', 'Peter', 'Barry']
heroes = ['Batman', 'Superman', 'Spiderman', 'Flash']

# print(zip(names, heroes))

print({names[i]: heroes[i] for i in range(len(names)) })