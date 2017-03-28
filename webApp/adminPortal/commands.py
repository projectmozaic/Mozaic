import os.path
import sys

prompt = "> "

"""print "Enter the path to your dataset"
dataset = raw_input(prompt)"""

print "Enter command to run your model, like so: 'python model.py data.csv'"
command = raw_input(prompt)

#must check if script and data exist in image
commandParse = command.split()

if (len(commandParse) < 2):
	sys.exit("Invalid command to run mode.")

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
	print "none selected"

else:
	sys.exit("Not a valid option.")


#add the command to the docker file
