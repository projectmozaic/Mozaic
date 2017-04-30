import os.path
import os
from subprocess import call
from subprocess import check_output
import sys
import apt
import json

from subprocess import call


prompt = "> "
HOME = os.path.expanduser("~")
#git config --get remote.origin.url

print "What would you like to do? Enter the corresponding number:"
print """
	(1) Generate configuration file.
	(2) Run from configuration file.
	(3) Run from wizard.
"""
command = raw_input(prompt)

if (command.strip() == "1"): #Generate config
	print "Generating a configuration file..."
	print "Grabbing Python2 installed packages..."
	py27_installed_packages = check_output(["pip", "freeze"]).split()
	print py27_installed_packages
	print "Grabbing Python3 installed packages..."
	py34_installed_packages = check_output(["pip3", "freeze"]).split()
	print py34_installed_packages

	print "Grabbing linux packages..."
	cache = apt.Cache()
	linux_packages = [pkge.name for pkge in cache if pkge.is_installed]
	print linux_packages
	print "Package information received."


	print "\nEnter the git URL to your code base (Github) or root folder:"
	codePath = raw_input(prompt)

	print "\nEnter the URL to your dataset (ie, on S3) or path to file:"
	dataset = raw_input(prompt)

	print "\nEnter main command to run from root directory of code base: "
	command = raw_input(prompt)

	while 1:
		print "\nSelect one of the following options for running your model: AWS, MOC, None"
		cloud = raw_input(prompt)

		if (cloud.lower() == "aws"):
			print "AWS selected"
			break

		elif (cloud.lower() == "moc"):
			print "MOC selected"
			break

		elif (cloud.lower() == "none"):
			print "None selected. Will run command locally.\n"
			break
		else:
			print "Not a valid option."

	username = ''
	password = ''
	if cloud.lower() != "none":
		print "\nEnter credentials for your selected cloud vendor: "
		username = raw_input(prompt+" Username: ")
		password = raw_input(prompt+" Password: ")

	with open(HOME+'/configuration.json', 'w') as configurationFile:
		configurationFile.write(
				'{\n\t"python 2.7": ' + str(py27_installed_packages).replace("'", '"') +
				',\n\t"python 3.4": ' + str(py34_installed_packages).replace("'", '"') +
				',\n\t"apt-get": ' + str(linux_packages).replace("'", '"')+
				',\n\t"coderepo": "' + codePath +
				'",\n\t"commands": "' + command +
				'",\n\t"dataset": "' + dataset +
				'",\n\t"cloud": "' + cloud.lower() +
				'",\n\t"credentials": ' +
					'\n{ "username": "'+ username + '", "password": "' + password +
				'"}\n}')

	print "Configuration file written to ~/configuration.json"
		
elif (command.strip() == "2"): #Parse configuration file
	print "Enter full path of configuration file. Default = ~/configuration.json"
	path = raw_input(prompt)

	try:
		if path.strip():
			configurationFile = open(path, 'r')
			print "Read " + path
		else:
			configurationFile = open(HOME+'/configuration.json', 'r')
			print "Read ~/configuration.json"
	except:
		sys.exit("File cannot be opened")

	configuration = json.load(configurationFile)
	if configuration['cloud'] == "none":
		command = configuration['commands']+" "+configuration['dataset']
		try:
			call(command.split())
		except:
			print "Failed to run commands."


elif (command.strip() == "3"): #Ask user questions to run code one time
	print "Enter command to run your model, like so: 'python model.py data.csv'"
	command = raw_input(prompt)

	#must check if script and data exist in image
	commandParse = command.split()

	if (len(commandParse) < 2):
		sys.exit("Invalid command to run model.")

	script = "./" + commandParse[1]
	if (os.path.isfile(script) == False):
		sys.exit("Model file does not exist.")

	if (len(commandParse) == 3):
		model = "./" + commandParse[2]
		if (os.path.isfile(model) == False):
			sys.exit("Data file does not exist.")


	print "Select one of the following options for running your model: AWS, MOC, OpenStack, None"
	cloud = raw_input(prompt)

	if (cloud.lower() == "aws"):
		print "aws selected"

	elif (cloud.lower() == "moc"):
		print "moc selected"

	elif (cloud.lower() == "openstack"):
		print "openstack selected"

	elif (cloud.lower() == "none"):
		print "None selected. Will run command locally.\n"
		call(commandParse)

	else:
		sys.exit("Not a valid option.")
#must check if script and data exist in image
commandParse = command.split()

if (len(commandParse) < 2):
	sys.exit("Invalid command to run model.")


script = "./" + commandParse[1]
if (os.path.isfile(script) == False):
    sys.exit("Model file does not exist.")

if (len(commandParse) == 3):
    model = "./" + commandParse[2]
    if (os.path.isfile(model) == False):
        sys.exit("Data file does not exist.")

call(commandParse);

print "Select one of the following options for running your model: AWS, MOC, OpenStack, None"
cloud = raw_input(prompt)

if (cloud.lower() == "aws"):
    print "aws selected"

elif (cloud.lower() == "moc"):
    print "moc selected"

elif (cloud.lower() == "openstack"):
    print "openstack selected"

elif (cloud.lower() == "none"):
    print "none selected"

else:
    sys.exit("Not a valid option.")


#add the command to the docker file