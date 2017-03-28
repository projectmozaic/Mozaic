#External functions we might need for processing
import tempfile
import os
import hashlib
import csv
import json
from subprocess import call
import shutil

def makeDockerFile(py27, py34, rpacks, gitrepo, aptget, fileDirectory, packageFile):
    tmpDocker = open(fileDirectory+"/Dockerfile", "w+")
    tmpDocker.write("FROM ubuntu:latest\n") #Base image is ubuntu
    tmpDocker.write('''
RUN apt-get update -q && apt-get install -yqq \\
    apt-utils \\
    git \\
    ssh \\
    gcc \\
    make \\
    build-essential \\
    libkrb5-dev \\
    sudo
''')

    if (len(packageFile) > 0):
        #parse csv files
        if (packageFile.name[-3:] == "csv"):
            data = [row for row in csv.reader(packageFile.read().splitlines())]
            for item in data:
                if item[0].lower() == "python 2.7":
                    tmpDocker.write("RUN apt-get install -y python python-dev python-distribute python-pip\n")
                    for package in item[1:]:
                        tmpDocker.write("RUN pip "+package.lower()+"\n")
                if item[0].lower() == "python 3.4":
                    tmpDocker.write("RUN apt-get install -y python-pip3\n")
                    for package in item[1:]:
                        tmpDocker.write("RUN pip3 " + package + "\n")

        if (packageFile.name[-4:] == "json"):
            data = json.loads(packageFile.read())
            packages = {}
            for key, value in data.iteritems():
                packages[key.lower()] = value
            if "python 2.7" in packages:
                tmpDocker.write("RUN apt-get install -y python python-dev python-distribute python-pip\n")
                installs = [item.strip() for item in packages["python 2.7"][0].split(",")]
                for package in installs:
                    tmpDocker.write("RUN pip "+package.lower()+"\n")
                    print("RUN pip "+package.lower()+"\n")
            if "python 3.4" in packages:
                tmpDocker.write("RUN apt-get install -y python-pip3\n")
                installs = [item.strip() for item in packages["python 3.4"][0].split(",")]
                for package in installs:
                    tmpDocker.write("RUN pip3 " + package + "\n")
                    print("RUN pip3 " + package + "\n")

    if (len(py27) > 0 and py27[0] == "python") :
        tmpDocker.write("RUN apt-get install -y python python-dev python-distribute python-pip\n")
        for packages in py27[1:]:
            tmpDocker.write("RUN pip "+packages+"\n")

    if (len(py34) > 0 and py34[0] == "python"): #Python3.4 is default installed
        tmpDocker.write("RUN apt-get install -y python-pip3\n")
        for packages in py34[1:]:
            tmpDocker.write("RUN pip3 " + packages + "\n")

    for gitURL in gitrepo:
        url = gitURL.strip()
        if url != '':
            tmpDocker.write("RUN git clone "+ url+ "\n")

    for package in aptget:
        package = package.strip()
        if package != '':
            tmpDocker.write("RUN apt-get install "+ package+ "\n")

    files = os.listdir(fileDirectory)

    for file in files:
        if file != "Dockerfile":
            tmpDocker.write("ADD "+"./"+file+" /files\n")
            
    tmpDocker.write("VOLUME /files\n")
    tmpDocker.write("CMD [\"python\", \"./commands.py\"]\n")
    tmpDocker.seek(0)
    print tmpDocker.read()
    tmpDocker.close()

def makeDockerImage(fileDirectory):
    with cd(fileDirectory):
        call("ls -al", shell=True)
        m = hashlib.md5()
        m.update(fileDirectory)
        # This path for calling the docker daemon will probably be changed on our instance
        # but this is the default path for now on my mac
        tempfile = m.hexdigest().lower()
        print tempfile
        call("eval $(/usr/local/bin/docker-machine env default) &&"+
             " sleep 2 && docker build -t "+tempfile+" .", shell=True)
        call("eval $(/usr/local/bin/docker-machine env default) && docker save "+tempfile+" > tempimg.tar", shell=True)

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)