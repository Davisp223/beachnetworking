from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


def index(request):
    return render(request, 'index/index.html')

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


def login(request):
     form = MyForm()