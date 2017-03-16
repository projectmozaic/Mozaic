import subprocess
import os
os.chdir("/Users/weijiang/Desktop/CS528 Cloud Computing//Project/Sprint2/goldimage/update/")
str = subprocess.call('ls', shell=True)
str = subprocess.call('docker build -t goldimage .', shell=True)
