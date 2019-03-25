from django import forms
from .models import Bussiness

class CreateBussiness(forms.ModelForm):
    class Meta:
       model = Bussiness
       fields = ['photo','neighbourhood','name']

