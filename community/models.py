from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    hood_location = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(User)

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to='profile/')
    neighbourhood = models.ForeignKey('Neighbourhood',blank=True,null=True)
    contact =models.CharField(max_length=100,bank=True)

class Bussiness(models.Model):
    photo = models.ImageField(upload_to='bussiness/',default='bussiness/bdefault.jpg')
    name = models.CharField(max_length)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey('Neighbourhood',related_name='business')
    email = models.CharField(max_length=30)




