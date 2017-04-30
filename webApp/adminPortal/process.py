#External functions we might need for processing
import tempfile
import os
import hashlib
import csv
import json
from subprocess import call
import shutil
import sys

def makeDockerFile(py27, py34, rpacks, gitrepo, aptget, fileDirectory, packageFile):
    tmpDocker = open(fileDirectory+"/Dockerfile", "w+")
    tmpDocker.write("FROM ubuntu:latest\n") #Base image is ubuntu
    tmpDocker.write('''
RUN apt-get update -q && apt-get install -yqq \\
    apt-utils \\
    git \\
    vim \\
    nano \\
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
            if "python 3.4" in packages:
                tmpDocker.write("RUN apt-get install -y python-pip3\n")
                installs = [item.strip() for item in packages["python 3.4"][0].split(",")]
                for package in installs:
                    tmpDocker.write("RUN pip3 " + package + "\n")

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
            tmpDocker.write("ADD "+"./"+file+" /src\n")
            
    #tmpDocker.write("VOLUME /files\n")
    call(["cp", "./adminPortal/commands.py", fileDirectory])
    tmpDocker.write("ADD ./commands.py /")
    tmpDocker.seek(0)
    print tmpDocker.read()
    tmpDocker.close()


def updateImage(py27, py34, rpacks, gitrepo, aptget, fileDirectory, packageFile, imageFile):
    try:
        if (imageFile.name[-3:] != "tar"):
            retcode = call('docker load -i ' + imageFile.name + '.tar', shell=True)
        else:
            retcode = call('docker load -i ' + imageFile.name, shell=True)
        if retcode < 0:
            print >>sys.stderr, "Subprocess was terminated by signal", -retcode2
        else:
            print >>sys.stderr, "Subprocess returned", retcode
        # fp = tempfile.TemporaryFile()
        with open('Dockerfile', 'wb') as tmpDocker:
            tmpDocker.write('FROM '+imageFile.name + ':latest\n')
            files = os.listdir(fileDirectory)
            for file in files:
                if file != "":
                    tmpDocker.write('ADD ' + i + ' /\n')

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
                        if "python 3.4" in packages:
                            tmpDocker.write("RUN apt-get install -y python-pip3\n")
                            installs = [item.strip() for item in packages["python 3.4"][0].split(",")]
                            for package in installs:
                                tmpDocker.write("RUN pip3 " + package + "\n")

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

            """if pipPackge != "":
                fp.write('RUN pip install ' + pipPackge  + '\n')
            if git_packages_url != "":
                fp.write("RUN git clone "+ git_packages_url+ "\n")
            if aptGet_packages != "":
                fp.write("RUN apt-get install "+ aptGet_packages + "\n")"""
        # fp.write('ADD ' + filesToAdd + ' /\n')
        ok = call('docker build -t tempimage1 .', shell=True)
        if ok < 0:
            print >>sys.stderr, "Subprocess was terminated by signal", -ok
        os.remove('Dockerfile')
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e

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

def parseConfig(fileDirectory, configString, fileName):
    #overwrite json file with new data
    with open(fileName, 'w') as outfile:
        json.dump(json.loads(configString), outfile)

    #create docker file
    tmpDocker = open(fileDirectory+"/Dockerfile", "w+")
    tmpDocker.write("FROM ubuntu:latest\n") #Base image is ubuntu
    tmpDocker.write('''
    RUN apt-get update -q && apt-get install -yqq \\
        apt-utils \\
        git \\
        vim \\
        nano \\
        ssh \\
        gcc \\
        make \\
        build-essential \\
        libkrb5-dev \\
        sudo
    ''')

    data = json.loads(configString)
    group = {}
    for key, value in data.iteritems():
        group[key.lower()] = value
    if "python 2.7" in group:
        tmpDocker.write("RUN apt-get install -y python python-dev python-distribute python-pip\n")
        installs = [item.strip() for item in group["python 2.7"][0].split(",")]
        for package in installs:
            tmpDocker.write("RUN pip "+package.lower()+"\n")
    if "python 3.4" in group:
        tmpDocker.write("RUN apt-get install -y python-pip3\n")
        installs = [item.strip() for item in group["python 3.4"][0].split(",")]
        for package in installs:
            tmpDocker.write("RUN pip3 " + package + "\n")
    if "code repo" in group:
        installs = [item.strip() for item in group["code repo"][0].split(",")]
        for repo in installs:
            url = repo.strip()
            if url != '':
                tmpDocker.write("RUN git clone "+ url+ "\n")
    if "data set" in group:
        print "data set"
    if "main command" in group:
        print "main command"
            
    #tmpDocker.write("VOLUME /files\n")
    tmpDocker.write("ADD commands.py /\n")
    tmpDocker.write("ADD " + fileName + " /")
    tmpDocker.seek(0)
    print tmpDocker.read()
    tmpDocker.close()


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)