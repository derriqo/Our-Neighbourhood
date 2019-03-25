from django import forms
from .models import Bussiness,Profile

class CreateBussiness(forms.ModelForm):
    class Meta:
       model = Bussiness
       fields = ['photo','neighbourhood','name']

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','neighbourhood','email']