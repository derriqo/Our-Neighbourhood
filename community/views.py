from django.shortcuts import render
from .models import Profile,Neighbourhood,Bussiness
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'index.html')


@login_required(login_url='accounts/')
def profile(request):
    current__user = request.user
    return render(request,'profile/profile.html')