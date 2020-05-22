from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())

parser['SETTINGS'] = {
	'SECRET_KEY': 'sdjih32iyTUYR45YTFrtdgggf__gf54F5gh3',
	'APIKEY': 'jg2344wewdw34t34ff3kjrjcr32j3423',
	'DEFAULT_USER': 'default',
	'DEFAULT_PASS': 'default_pass',
	'PYTHON_VERSION': 3,
	'BASE_PATH': '/usr/lib/'
}

parser['DATABASE'] = {
	'HOST': 'localhost',
	'DB_USER': 'root',
	'DB_PASS': 'password',
	'DB_NAME': 'test'	
}

parser['FILES'] = {
	'PYTHON_PATH': '%{settings:base_path}spython%(settings:python_version)s'
}

with open('config.ini', 'w') as file:
	parser.write(file)