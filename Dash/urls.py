"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from DashApp import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('', views.LoginPage, name='login'),  # Page de connexion
    path('password/', views.change_password, name='change_password'),
    path('index/',views.HomePage,name='index'),
    path('logout/',views.LogoutPage,name='logout'),  
    path('lire-fichierso/', views.readfileso, name='readfileso'),
    path('lire-fichiertn1/', views.readfiletn1, name='readfiletn1'),
    path('lire-fichiertn2/', views.readfiletn2, name='readfiletn2'),
    path('lire-fichierint/', views.readfileint, name='readfileint'),
    path('lire-fichiersoapn/', views.readfilesoapn, name='readfilesoapn'),
    path('lire-fichiertn1apn/', views.readfiletn1apn, name='readfiletn1apn'),
    path('lire-fichiertn2vepgapn/', views.readfiletn2vepgapn, name='readfiletn2vepgapn'),
    path('lire-fichiertn2apn/', views.readfiletn2apn, name='readfiletn2apn'),
    path('lire-fichiersoepg/', views.readfilesoepg, name='readfilesoepg'),
    path('lire-fichiertn1epg/', views.readfiletn1epg, name='readfiletn1epg'),
    path('lire-fichiertn2epg/', views.readfiletn2epg, name='readfiletn2epg'),
    path('lire-fichiertn2vepg/', views.readfiletn2vepg, name='readfiletn2vepg'),

    path('mme/', views.mme_view, name='mme'),
    path('int/', views.int_view, name='int'),
    path('global/', views.global_view, name='global'),
    path('epg/', views.epg_view, name='epg'),
    path('apn/', views.apn_view, name='apn'),
    
    path('update_table/', views.HomePage, name='update_table'),
    

]
