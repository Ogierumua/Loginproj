from . import views
from django.urls import path
#from django.contrib import admin
from django.urls import include



urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    
]
