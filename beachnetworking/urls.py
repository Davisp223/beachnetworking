"""beachnetworking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from index import views as index_views
from index.views import CustomPasswordResetView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('index.urls'), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index/logout.html'), name='logout'),
    path('register/', index_views.register, name='register'),
    path('estimate/', index_views.estimate, name='estimate'),

    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    
    #path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
