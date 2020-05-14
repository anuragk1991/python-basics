import os
from contextlib import contextmanager


@contextmanager
def changedir(path):
	'''
	Context Manager using function to change to given path and then switch back to original path

	'''
	cwd = os.getcwd()
	try:
		os.chdir(path)
		yield
	finally:
		os.chdir(cwd)


with changedir('oops'):
	print(os.listdir())

with changedir('env'):
	print(os.listdir())


class ChangeDir:
	'''
	Context Manger using class to switch to given path. On exit switch back to original path
	'''
	def __init__(self, path):
		self.path = path
		self.cwd = os.getcwd()

	def __enter__(self):
		os.chdir(self.path)

	def __exit__(self, exc_type, exc_value, traceback):
		os.chdir(self.cwd)


with ChangeDir('oops'):
	print('Listing files and folders')
	print(os.listdir())


print("After Exit")
print('Listing items in current directory')
print(os.listdir())
