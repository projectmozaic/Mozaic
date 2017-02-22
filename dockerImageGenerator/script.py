import subprocess
import ConfigParser

# Read conf file
config = ConfigParser.RawConfigParser()
configFilePath = 'config.conf'
config.read(configFilePath)

lang = config.get('Section', 'lang')
dataset = config.get('Section','dataset')
script = config.get('Section', 'script')
packages = config.get('Section', 'package')
# Write Dockerfile
with open('Dockerfile', 'wb') as f:
	# Set Language
	if lang == 'python2.7':
		f.write("FROM python:2.7\n")
	# Set dataset
	f.write('ADD ' + dataset + ' /\n')
	# Set script
	f.write('ADD ' + script + ' /\n')
	# Set command
	if lang == 'python2.7':
		packages = packages.split(',')
		for package in packages:
			package = package.strip()
			package_command = 'RUN pip install ' + package  + '\n'
			f.write(package_command)
	exe_command = 'CMD python ' + script + '\n'
	f.write(exe_command + '\n')
# Make the docker image
str = subprocess.call('docker build -t tempimage .', shell=True)