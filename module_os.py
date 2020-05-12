import os
from datetime import datetime

print('OS Module')
print('')

print('Print Current Working Directory using os.getcwd()')
print(os.getcwd())
print('')

print('Change directory using os.chdir() to /home/anurag/Code')
print('Now print Current Working Directory')
os.chdir('/home/anurag/Code/')
print(os.getcwd())
print('')

print('Get list of directories and files using os.listdir(). Note:In python 2, it is mandatory to pass an argument (dirpath) whereas it is optional in python 3, if not provided it will list the files and directories of current working directory')
print(os.listdir())
print('')

print('Create Directory')
print('Using os.mkdir(). Create a directory named Demo. Note: It will throw an error if the directory already exists')
os.rmdir('Demo')
os.mkdir('Demo')

try:
	print("os.mkdir('New/Demo') will throw an error since New folder doesn\'t exists")
	os.removedirs('New/Demo')
	os.mkdir('New/Demo')
except FileNotFoundError:
    print('Error in creating nested directory, Folder doesn\'t exists')
    print('')

print('Using os.makedirs(). Create a directory named Demo. Note: It will also create nested directories if they don\'t exists')

os.makedirs('New/Demo')
print(os.listdir())
print('')

print(os.listdir())
print('Rename file using os.rename(), Lets rename test.txt to demo.txt')
os.rename('test.txt', 'demo.txt')
print(os.listdir())
os.rename('demo.txt', 'test.txt')
print('')

print('Details of file using os.stat()')
file_details = os.stat('test.txt')
print(file_details)
timestamp = file_details.st_mtime

print('st_size: Size of file in bytes, st_mtime: last modified date, etc')
print('Size: {} bytes'.format(file_details.st_size))
print('Modified Timestamp: {}'.format(timestamp))
print('Convert timestamp to readable datetime format')
print('Modified Date: {}'.format(datetime.fromtimestamp(timestamp)))
