from django.shortcuts import render,redirect
from .models import Profile,Neighbourhood,Bussiness
from django.contrib.auth.decorators import login_required
import datetime as dt
from .forms import CreateBussiness
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'index.html')


@login_required(login_url='accounts/')
def profile(request):

    profile = Profile.objects.get(user=request.user)
    hoods = Neighbourhood.objects.all()

    return render(request,'profile/profile.html', {'profile':profile , 'hoods':hoods} )

# def edit_profile(request):
#     date = dt.date.today()
#     current_user = request.user
#     profile = Profile.objects.get(user=current_user.id)
#     if request.method == 'POST':
#         signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
#         if signup_form.is_valid():
#             signup_form.save()
#             return redirect('profile')
#     else:
#         signup_form =EditForm() 
        
#     return render(request, 'profile/update_profile.html', {"date": date, "form":signup_form,"profile":profile})

@login_required(login_url='accounts/')
def new_bussiness(request):

    if request.method=='POST':
        form = CreateBussiness(request.POST,request.FILES)
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.user = request.user
            bussiness.profile = request.user.profile
            bussiness.save()
            return redirect ('biz_page')
    else:
        form = CreateBussiness()
            
    return render(request,'addbussiness.html',{'form':form}) 

def biz_page(request):
    bussinesses = Bussiness.objects.all()
    return render(request,'bussinesspage.html', {'bussinesses':bussinesses} )
