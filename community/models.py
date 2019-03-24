from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to='profile/')
    neighbourhood = models.ForeignKey('Neighbourhood',blank=True,null=True)
    contact =models.CharField(max_length=100,blank=True)
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30,blank=True)
    hood_location = models.CharField(max_length=30,blank=True)
    occupants_count = models.IntegerField(default=0,blank=True)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True)

class Bussiness(models.Model):
    photo = models.ImageField(upload_to='bussiness/',default='bussiness/bdefault.jpg')
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey('Neighbourhood',related_name='businesses')
    profile = models.ForeignKey(Profile, related_name='profiles')
    email = models.CharField(max_length=30)





