from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GenerateForm
from .forms import CheckForm
import process


# Create your views here.

def index(request):
    if (request.method == "POST"):
        form = GenerateForm(request.POST)
        if form.is_valid():
            print request.FILES['file']
            print request.FILES['file'].read()
            return HttpResponseRedirect('/success')
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
    return render(request, 'index.html', {'posted': "Failed"})

"""def get_forms(request):
    if request.method == 'POST':
        form = py27Form(request.POST)
        if form.is_valid():
            print("checkboxd")
            return HttpResponseRedirect('/generate')
    else:
        return render(request, 'index.html', {})"""

def generate(request):
    if request.method == 'POST':
        py27 = request.POST.getlist('python27')
        py34 = request.POST.getlist('python34')
        print "Python 2.7:"
        for packages in py27:
            print packages
        print "Python 3.4:"
        for packages in py34:
            print packages

        print "Files:"
        for item in request.FILES.getlist("file[]"):
            print item.read()

        return render(request, 'index.html', {'posted': "Valid"})
    #else:
    return render(request, 'index.html', {})