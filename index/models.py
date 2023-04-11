from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Estimate(models.Model):

    Services = (
     ('Network Instalation', 'Network Instalation'),
     ('Server Instalation', 'Server Instalation'),
     ('Cable Running / Managment', 'Cable Running / Managment'),
     ('Smart Home', 'Smart Home'),
     ('Other', 'Other'),
    )

    Contact = (
     ('Email', 'Email'),
     ('Phone', 'Phone'),
    )


    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=30, blank=True)
    Phone_number =  models.CharField(blank=True, max_length=40)
    prefered_contact_method = models.CharField(blank=False,max_length=100,null=False, default='Email',choices=Contact)
    Address =  models.CharField(blank=True,max_length=100)
    Service =  models.CharField(blank=False,max_length=40,null=False, default='Network Instalation',choices=Services)
    Other_service =  models.CharField(blank=True,max_length=100)
    Deadline =  models.CharField(blank=True,max_length=100)
    Budget =  models.CharField(blank=True,max_length=100)
    Aditional_comments =  models.TextField(blank=True,)
    Deadline =  models.CharField(blank=True,max_length=100)
    How_Did_You_Hear_About_Us =  models.CharField(blank=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.company_name} - {self.name}'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

