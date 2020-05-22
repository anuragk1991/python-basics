from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

print(parser.get('SETTINGS', 'PYTHON_VERSION'))