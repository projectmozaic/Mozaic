from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import GenerateForm
from .forms import CheckForm
from .process import makeDockerFile

import tempfile
from subprocess import call


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
        gitrepo = request.POST.getlist('gitRepo')
        aptget = request.POST.getlist('aptget')

        fileDirectory = tempfile.mkdtemp()
        for item in request.FILES.getlist("file[]"):
            #print item.name
            with open(fileDirectory+"/"+item.name, 'wb+') as destination:
                destination.write(item.read())

        makeDockerFile(py27, py34, rpacks, gitrepo, aptget, fileDirectory)
        return redirect('/process', fileDirectory="fileDirectory")
    #else:
    return render(request, 'index.html', {})

def process(request):
    return render(request, 'process.html')