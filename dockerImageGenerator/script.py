# This script makes the dockerfile from the configure file then generate the docker image(named tempimage).
# Settings supported: python 2.7, csv dataset.

import subprocess
import ConfigParser

# Read conf file
config = ConfigParser.RawConfigParser()
configFilePath = 'config.conf'
config.read(configFilePath)

lang = config.get('Section', 'lang')
dataset = config.get('Section','dataset')
script = config.get('Section', 'script')

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
		command = 'CMD [ \"python\", \"./' + script + '\" ]'
	f.write(command + '\n')
# Make the docker image
str = subprocess.call(['sudo', 'docker', 'build', '-t', 'tempimage', '.'])
