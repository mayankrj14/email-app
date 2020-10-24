#from django.shortcuts import render,
from django.http import HttpResponse 

#User and login imports
from django.contrib.auth import authenticate, login, logout

#created module
from .extra import (
    create_user,
)


def home_view(request):             #
    return HttpResponse('<h1>Hello, World!</h1>Home')
    

#Login and Logout
def login_view(request):            #Login

    if request.method == "POST":
        username_   = request.POST.get('username')
        password_   = request.POST.get('password')

        user = authenticate(username = username_, password = password_)
        
        if user is not None:
            login(request, user)
            #Page ReDirect
        else:
            pass
            # Warning/ReCheck Message
    return HttpResponse('<h1>Hello, World!</h1>Login')

def logout_view(request):           #Logout
    logout(request)
    #Page ReDirect


#SignUp
def signup_view(request):           #SignUp

    if request.method == "POST":
        pass

    return HttpResponse('<h1>Hello, World!</h1>Signup')


def email_sender_view(request):     #POST Request Form
    return HttpResponse('<h1>Hello, World!</h1>email_sender')