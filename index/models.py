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


    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=30, blank=True)
    Phone_number =  models.CharField(blank=True, max_length=40)
    Address =  models.CharField(blank=True,max_length=100)
    Service =  models.CharField(blank=False,max_length=40,null=False, default='Network Instalation',choices=Services)
    Other_service =  models.CharField(blank=True,max_length=30)
    Deadline =  models.CharField(blank=True,max_length=30)
    Budget =  models.CharField(blank=True,max_length=30)
    Aditional_comments =  models.TextField(blank=True,)
    Deadline =  models.CharField(blank=True,max_length=30)
    How_Did_You_Hear =  models.CharField(blank=True,max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields for your user profile here
    company_name = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

