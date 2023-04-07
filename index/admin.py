from django.contrib import admin
from .models import Feedback, UserProfile,Estimate

from django.contrib.auth import get_user_model
# Register your models here.



admin.site.register(Feedback)
admin.site.register(UserProfile)
admin.site.register(Estimate)