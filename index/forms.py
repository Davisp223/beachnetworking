from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Feedback, Estimate



class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        company_name = forms.CharField(max_length=30, )

        
        class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name','company_name', 'password1', 'password2']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')


class EstimateForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ('name', 'email','company_name','Phone_number','Address','Service','Other_service','Deadline','Budget','Aditional_comments','Deadline','How_Did_You_Hear')
