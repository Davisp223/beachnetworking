from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.urls import reverse_lazy
from .models import UserProfile, Feedback
from .forms import  EstimateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Feedback, Estimate, UserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.views.generic import (
     CreateView,
)


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Thanks for contacting us {name} We will get with you shortly!')
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'index/index.html', {'form': form})


def custom_404(request, exception):
    return render(request, 'index/404.html', status=404)

def tos(request):
    return render(request, 'index/tos.html')

def privacy(request):
    return render(request, 'index/privacy.html')


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
            name = request.POST.get('name')
            company_name = request.POST.get('company_name')

            messages.success(request, f'Thanks for submitting an estimate. We have sent you an email confirming your estimate.')
            subject = 'Estimate Confirmation'
            message = f'Thank you for submiting and estimate, {name}!\n\nWe have received your estimate for {company_name}\n\nOne of our associates will be in contact with you shortly to discuss your estimate.  Thank You again.'
            from_email = 'no-reply@beachnetworking.com'
            recipient_list = [request.POST.get('email')]
            send_mail(subject, message, from_email, recipient_list)

            subject2 = 'Estimate Submission'
            message2 = f'There has been an estimate submitted by {name} for {company_name} please check the website for more details.'
            from_email2 = 'no-reply@beachnetworking.com'
            recipient_list2 = ('davis@beachnetworking.com','colin@beachnetworking.com')
            send_mail(subject2, message2, from_email2, recipient_list2)
            return redirect('index')

    return render(request, 'index/estimate.html', {'form': form})




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save the company name to the user's profile
            user.userprofile.company_name = form.cleaned_data.get('company_name')
            user.userprofile.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'index/register.html', {'form': form})



class CustomPasswordResetView(PasswordResetView):
    template_name = 'index/password_reset_form.html'  # your custom template
    email_template_name = 'index/password_reset_email.html'  # your custom email template
    subject_template_name = 'index/password_reset_subject.txt'  # your custom subject template
    success_url = reverse_lazy('password_reset_done')  # your custom success url

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'index/password_reset_done.html'  # your custom template
    success_url = reverse_lazy('password_reset_done')  # your custom success url

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'index/password_reset_complete.html'  # your custom template
    success_url = reverse_lazy('password_reset_done')  # your custom success url

class CustomPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'index/password_reset_confirm.html'  # your custom template
    email_template_name = 'index/password_reset_email.html'  # your custom email template
    subject_template_name = 'index/password_reset_subject.txt'  # your custom subject template
    success_url = reverse_lazy('password_reset_done')  # your custom success url