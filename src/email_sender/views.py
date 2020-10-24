#from django.shortcuts import render,
from django.http import HttpResponse 

#User and login imports
from django.contrib.auth.models import User


def home_view(request):             #
    return HttpResponse('<h1>Hello, World!</h1>Home')
    

def login_view(request):            #

    if request.method == "POST":
        user_name = request.POST.get('username')

        user = authenticate(username='john', password='secret')
        if user is not None:
            # LOGIN PROCESS
        else:
            # Warning/ReCheck Message


    return HttpResponse('<h1>Hello, World!</h1>Login')


def signup_view(request):           #

    if request.method == "POST":
        pass

    return HttpResponse('<h1>Hello, World!</h1>Signup')


def email_sender_view(request):     #POST Request Form
    return HttpResponse('<h1>Hello, World!</h1>email_sender')