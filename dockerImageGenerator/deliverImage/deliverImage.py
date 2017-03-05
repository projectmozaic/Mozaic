import subprocess
import ConfigParser

# Read conf file
config = ConfigParser.RawConfigParser()
configFilePath = 'config.conf'
goldConfig = '../goldImage/goldconfig.conf'
config.read(configFilePath)

lang = config.get('Section', 'lang')
dataset = config.get('Section','dataset')
script = config.get('Section', 'script')
package = config.get('Section', 'package')
packagelist = package.split()

config.read(goldConfig)
goldpackage = config.get('Section', 'package')
goldpackagelist = goldpackage.split()

delete = []
install = []

for idx, golditem in enumerate(goldpackagelist):
	if golditem not in packagelist:
		delete.append(golditem)

strdelete = ' '.join(delete)

# Write Dockerfile
with open('Dockerfile', 'wb') as f:
	# Set Language
	if lang == 'python2.7':
		f.write("FROM goldimage\n")
	# Set dataset
	f.write('ADD ' + dataset + ' /\n')
	# Set script
	f.write('ADD ' + script + ' /\n')
	# delete un-needed packages
	if lang == 'python2.7':
		if len(strdelete)>0:
			command = 'RUN pip uninstall -y ' + strdelete  + '\n' + 'CMD python ' + script
	f.write(command + '\n')
# Make the docker image
str = subprocess.call('docker build -t tempimage .', shell=True)
