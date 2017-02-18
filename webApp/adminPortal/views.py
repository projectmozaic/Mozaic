from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GenerateForm
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