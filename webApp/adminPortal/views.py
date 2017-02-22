from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GenerateForm
from .forms import CheckForm
import process

import os, tempfile, zipfile
from django.http import HttpResponse
from wsgiref.util import FileWrapper


# Create your views here.

def index(request):
    if (request.method == "POST"):
        form = GenerateForm(request.POST)
        if form.is_valid():
            print request.FILES['file']
            print request.FILES['file'].read()
            return HttpResponseRedirect('/success.html')
    else:
        return render(request, 'index.html', {})

#Ignore for now -- this will be for serving the image back
def success(request):
    if request.method == 'POST':
        form = GenerateForm(request.POST)

        for item in request.FILES.getlist("file[]"):
            print item.read()

        if form.is_valid():
            for item in request.FILES.getlist("file[]"):
                print item.read()
            return render(request, 'index.html', {'posted': "Valid"})
        else:
            form = GenerateForm()
    return render(request, 'success.html')


def generate(request):
    if request.method == 'POST':
        py27 = request.POST.getlist('python27')
        py34 = request.POST.getlist('python34')
        rpacks = request.POST.getlist('rcheck')
        gitrepo = request.POST.get('gitrepo')
        aptget = request.POST.get('aptget')
        #For debugging purposes!
        print "Python 2.7:"
        for packages in py27:
            print packages
        print "Python 3.4:"
        for packages in py34:
            print packages
        print "R 3.3.2:"
        for packages in rpacks:
            print packages;
        print "git repo:", gitrepo
        print "apt get:", aptget
        print "Files:"
        for item in request.FILES.getlist("file[]"):
            print item.read()

        return render(request, 'index.html', {'posted': "Valid"})
    #else:
    return render(request, 'index.html', {})

def process(request):
    return render(request, 'process.html')