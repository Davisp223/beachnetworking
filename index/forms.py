from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feedback, Estimate

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email','first_name','last_name','company_name',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')


class EstimateForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ('name', 'email','company_name','Phone_number','prefered_contact_method','Address','Service','Other_service','Deadline','Budget','Aditional_comments','Deadline','How_Did_You_Hear_about_us')
