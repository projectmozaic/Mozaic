from django import forms
from .models import PythonPackages

class GenerateForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PythonPackagesForm(forms.ModelForm):
    PythonPackages = forms.BooleanField()

    class Meta:
        model = PythonPackages
        fields = '__all__'
