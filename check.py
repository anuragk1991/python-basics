import logging
import time
from functools import wraps

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def my_logger(function):
	handler = logging.FileHandler('{}.log'.format(function.__name__))
	handler.setFormatter(formatter)
	logger = logging.getLogger(function.__name__)
	logger.setLevel(logging.INFO)
	logger.addHandler(handler)

	@wraps(function)
	def wrapper():
		logger.info('Executing {} function'.format(function.__name__))
		return function()

	return wrapper

def my_timer(function):
	@wraps(function)
	def wrapper():
		t1 = time.time()
		result = function()
		t2 = time.time()

		print('{} function executed in {} seconds'.format(function.__name__, t2 - t1))
		return result

	return wrapper

@my_logger
@my_timer
def display():
	time.sleep(1)
	print('Disply function ran')



@my_logger
@my_timer
def run():
	time.sleep(1)
	print('Run function ran')

display()
run()