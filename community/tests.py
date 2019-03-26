from django.test import TestCase
from .models import Profile,Neighbourhood,Bussiness
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(username='derrick',email='derrick@gmail.com',password='qwerty123')
        self.user.save()

        self.derrick= Profile(profile_pic ='derrick.jpg',bio='junior developer',neighbourhood_id=1,email='derrick@gmail.com',  user=self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.derrick, Profile))

    #Testing Save Method
    def test_save_method(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_create_method(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.user=User(username='derrick',email='derrick@gmail.com',password='qwerty123')
        self.user.save()
        self.derrick= Profile(profile_pic ='derrick.jpg',bio='junior developer',neighbourhood_id=1,email='derrick@gmail.com',  user=self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()

    #Tests
    def test_save_profile(self):
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)
