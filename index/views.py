from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserRegisterForm, EstimateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Feedback, Estimate, UserProfile
from django.contrib.auth.views import PasswordResetView
from django.views.generic import (
     CreateView,
)


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'index/index.html', {'form': form})





@login_required
def estimate(request):
    # Get the user and user profile data
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    # Create a form instance with initial data
    initial_data = {
        'name': user.first_name + ' ' + user.last_name,
        'email': user.email,
        'company_name': user_profile.company_name if user_profile else None,
    }
    form = EstimateForm(request.POST or None, initial=initial_data)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'index/estimate.html', {'form': form})





def register(request):
    if request.method == 'POST': 
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your Account Has Been Created {username} You Are Now Able To Login!')
                return redirect ('login')
    else:
        form = UserRegisterForm()
    return render(request, 'index/register.html', {'form': form},)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'index/password_reset_form.html'  # your custom template
    email_template_name = 'index/password_reset_email.html'  # your custom email template
    subject_template_name = 'index/password_reset_subject.txt'  # your custom subject template
    success_url = reverse_lazy('password_reset_done')  # your custom success url