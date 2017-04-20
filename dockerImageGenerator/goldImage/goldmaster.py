import subprocess
import ConfigParser

# Read conf file
config = ConfigParser.RawConfigParser()
configFilePath = 'goldconfig.conf'
config.read(configFilePath)

lang = config.get('Section', 'lang')
package = config.get('Section', 'package')
# Write Dockerfile
with open('Dockerfile', 'wb') as f:
	# Set Language
	if lang == 'python2.7':
		f.write("FROM python:2.7\n")
	#Add log py file
	f.write('ADD ' + 'act_log.py' + ' /\n')
	f.write('ADD ' + 'log.txt' + ' /\n')
	f.write('ADD ' + 'Dockerfile' + ' /\n')
	f.write('RUN ' + 'python act_log.py' + '\n')
	# Set command
	if lang == 'python2.7':
		command = 'RUN pip install ' + package
	f.write(command + '\n')
# Make the docker image
str = subprocess.call('docker build -t goldimage .', shell=True)
