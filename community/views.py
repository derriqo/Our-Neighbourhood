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

def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/update_profile.html', {"date": date, "form":signup_form,"profile":profile})