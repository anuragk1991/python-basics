import time
import logging

#Decorator function
def decorator_function(function):
	def wrapper():
		print('wrapper executed')
		return function()
	return wrapper

@decorator_function
def display():
	print('my function')

# display()

#Decorator Class
class decorator_class():
	def __init__(self, function):
		self.function = function

	def __call__(self, *args, **kwargs):
		print('executed inside class')
		return self.function(*args, **kwargs)

@decorator_class
def display_class():
	print('display class func')

# display_class()


#Practical Examples

#1.Logging
def logger_function(function):
	"""To setup as many loggers as you want"""
	
	# logging.basicConfig(filename='{}.log'.format(function.__name__), level=logging.INFO)
	

	print('initializing logger {}'.format(function.__name__))

	def wrapper(*args, **kwargs):
		handler = logging.FileHandler('{}.log'.format(function.__name__))
		logger = logging.getLogger(function.__name__)
		logger.setLevel(logging.INFO)
		logger.addHandler(handler)
		
		logger.info('Executing {} function with parameters: {} and named parameters: {}'.format(function.__name__, args, kwargs))
		print('inside wrapper')
		return function(*args, **kwargs)

	return wrapper


@logger_function
def getUser(user_id):
	print('Fetching user with ID: {}'.format(user_id))

@logger_function
def setUser(*args, **kwargs):
	print('Setting user data: {}'.format(args))
	print('Setting user named parameters: {}'.format(kwargs))

getUser(5)
setUser(5, 10, name='Riju')
setUser(2, 1, name='Anurag')
setUser(4, 1002, name='Amit')


#2. Time elapsed to execute a function
def time_logger(function):
	import logging
	logging.basicConfig(filename='timelog.log'.format(function.__name__), level=logging.INFO)
	def wrapper(*args, **kwargs):
		
		t1 = time.time()
		result = function(*args, **kwargs)
		t2 = time.time()

		logging.info('Time Elapsed in executing {} function: {}'.format(function.__name__, t2 - t1))
		return result
	return wrapper

@time_logger
def test():
	time.sleep(3)
	print('Time function executed')

test()

@time_logger
def saveConfig():
	print('Saving Configurations')
	time.sleep(4)
	print('Configurations saved')

saveConfig()