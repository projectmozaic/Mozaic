from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import process
# Create your views here.


def index(request):
    if (request.method == "POST"):
        return render(request, 'index.html', {"posted": "Posted"})
    else:
        return render(request, 'index.html', {})

def submitted(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES['file']
            return render(request, 'index.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {})