from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import re


def index(request):
    return render(request, 'litelogapp/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username:
            messages.error(request, 'username can not be empty')
        if not password:
            messages.error(request, 'password can not be empty')
            
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'litelogapp/index.html', {'firstname':firstname})
        else:
            messages.error(request, 'bad credentials')
            
            return redirect('signin')
    return render(request, 'litelogapp/signin.html')
            
    
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeatpassword = request.POST.get('repeatpassword')
        
        if not username:
            messages.error(request, 'username can not be empty')
        elif not password:
            messages.error(request, 'password can not be empty')
        elif not firstname:
            messages.error(request, 'firstname can not be empty')
        elif not lastname:
            messages.error(request, 'lastname can not be empty')
        elif not email:
            messages.error(request, 'email can not be empty')
        elif not password:
            messages.error(request, 'password can not be empty')
        elif not repeatpassword:
            messages.error(request, 'repeat password can not be empty')
        
        elif User.objects.filter(username = username):
            messages.error(request, 'user already exist')
        elif User.objects.filter(email = email):
            messages.error(request, 'email already exit')
        elif len(username) > 25:
            messages.error(request, 'username can not be more than 25 characters')
        elif password != repeatpassword:
            messages.error(request, 'password is not same, Enter correct password')
        elif not username.isalnum():
            messages.error(request, 'username must be alphanumeric')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error('invalid email format')
            
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request, 'Your account have been created successfully')
            return redirect('signin')
    return render(request, 'litelogapp/signup.html')
            
            
         



def back(request):
    return render(request, 'litelogapp/index.html')

def signout(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully')
    return redirect (index)


    

# Create your views here.
