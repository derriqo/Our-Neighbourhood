from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    hood_location = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to='profile/')
    neighbourhood = models.ForeignKey('Neighbourhood',blank=True,null=True)

class Bussiness(models.Model):
    name = models.CharField(max_length)