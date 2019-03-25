from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    bio = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to='profile/')
    neighbourhood = models.ForeignKey('Neighbourhood',blank=True,null=True)
    email =models.EmailField(max_length=50,blank=True)
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_profile(sender, instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_profile(sender, instance,**kwargs):
        instance.profile.save()


class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30,blank=True)
    hood_location = models.CharField(max_length=30,blank=True)
    occupants_count = models.IntegerField(default=0,blank=True)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True)

    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save()

class Bussiness(models.Model):
    photo = models.ImageField(upload_to='bussiness/',default='bussiness/bdefault.jpg')
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey('Neighbourhood',related_name='businesses')
    profile = models.ForeignKey(Profile, related_name='profiles')
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name




