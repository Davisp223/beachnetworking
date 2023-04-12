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

from index.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirm, CustomPasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from index.sitemaps import MySitemap
from django.views.generic import TemplateView

sitemaps = {
    'my_sitemap': MySitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('index.urls'), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index/logout.html'), name='logout'),
    path('register/', index_views.register, name='register'),
    path('estimate/', index_views.estimate, name='estimate'),
    path('tos/', index_views.tos, name='tos'),
    path('privacy/', index_views.privacy, name='privacy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
handler404 = 'index.views.custom_404'
