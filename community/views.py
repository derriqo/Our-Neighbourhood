from django.shortcuts import render
from .models import Profile,Neighbourhood,Bussiness

# Create your views here.
def home(request):
    return render(request,'index.html')


# def profile(request):