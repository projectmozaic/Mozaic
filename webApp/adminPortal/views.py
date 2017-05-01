from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import smart_str
from django.template import loader
from .process import makeDockerFile, makeDockerImage, parseConfig, updateImage
from django.views.static import serve
import tarfile
import os

import tempfile
from subprocess import call
import shutil


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def config(request):
    if request.GET.get("processing"):
        if request.session['temp']:
            makeDockerImage(request.session['temp'])
            return HttpResponse()
        else:
            return "Error"
    return render(request, 'config_process.html')

def student(request):
    return render(request, 'student.html', {})

#Ignore for now -- this will be for serving the image back
def success(request):
    tempfile = request.session["temp"]+"/tempimg.tar"
    response = HttpResponse(open(tempfile, "rb").read(), content_type='application/x-tar')
    response['Content-Encoding'] = 'tar'
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("tempimg.tar")
    response['X-Sendfile'] = smart_str(tempfile)
    #shutil.rmtree(fileDirectory)
    return response


def generate(request):
    if request.method == 'POST':
        py27 = request.POST.getlist('python27')
        py34 = request.POST.getlist('python34')
        rpacks = request.POST.getlist('rcheck')
        gitrepo = request.POST.getlist('gitRepo')
        aptget = request.POST.getlist('aptget')

        print(request.FILES)
        print (request.POST)
        if len(request.FILES.getlist('fileselect')) > 0:
            packageFile = request.FILES.getlist('fileselect')[0];
        else:
            packageFile = ""

        fileDirectory = tempfile.mkdtemp()
        for i in range(len(request.FILES)):
            for item in request.FILES.getlist("file["+str(i)+"]"):
                print item.name
                with open(fileDirectory+"/"+item.name, 'wb+') as destination:
                    destination.write(item.read())

        makeDockerFile(py27, py34, rpacks, gitrepo, aptget, fileDirectory, packageFile)
        request.session['temp'] = fileDirectory
        print request.session['temp']
        return HttpResponse()
    #else:
    return render(request, 'index.html', {})

def process(request):
    if request.GET.get("processing"):
        if request.session['temp']:
            makeDockerImage(request.session['temp'])
            return HttpResponse()
        else:
            return "Error"
    return render(request, 'process.html')

def configedit(request):
    if request.method == 'POST':
        #try:
        if 1:
            text = request.POST.get('configinput')
            configfile = request.FILES.getlist('fileselect')[0].name;
            fileDirectory = tempfile.mkdtemp()
            parseConfig(fileDirectory, text, configfile)
            request.session['temp'] = fileDirectory
            return redirect("/config")
            #return render(request, 'config.html', {})
        #except:
            return render(request, 'config.html', {"error":"No file exists"})
    return render(request, 'config.html', {})


def imagestudent(request):
    if request.method == 'POST':
        try:
        #if 1:
            imageFile = request.FILES.getlist('imageselect')[0]
            fileDirectory = tempfile.mkdtemp()
            with open(fileDirectory+"/"+imageFile.name, 'wb+') as destination:
                    destination.write(imageFile.read())


        except:
            return render(request, 'student.html', {"error":"No image exists"})

        py27 = request.POST.getlist('python27')
        py34 = request.POST.getlist('python34')
        rpacks = request.POST.getlist('rcheck')
        gitrepo = request.POST.getlist('gitRepo')
        aptget = request.POST.getlist('aptget')
        if len(request.FILES.getlist('fileselect')) > 1:
            packageFile = request.FILES.getlist('fileselect')[1]
        else:
            packageFile = ""

        if (len(request.FILES.getlist("file[]")) > 0):
            for item in request.FILES.getlist("file[]"):
                with open(fileDirectory+"/"+item.name, 'wb+') as destination:
                    destination.write(item.read())

        updateImage(py27, py34, rpacks, gitrepo, aptget, fileDirectory, packageFile, imageFile)
        request.session['temp'] = fileDirectory
        print request.session['temp']
        return HttpResponse()

    return render(request, 'student.html')