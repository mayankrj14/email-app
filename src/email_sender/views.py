from django.shortcuts import (redirect, render,  )
from django.http import (HttpResponse, )

#User and login imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


#created module
from .extra import (
    create_user_,
    update_history,
)

def home_view(request):             #
    context = {
        
    }
    if request.user.is_authenticated:
        return redirect('Email')

    #update_history(request)
    return render(request, 'index.html', context)
    

#Login and Logout
def login_view(request):            #Login
    context = {
        
    }

    if request.method == "POST":
        username_   = request.POST.get('username')
        password_   = request.POST.get('password')

        print(username_,password_)
        user = authenticate(username = username_, password = password_)
        
        if user is not None:
            login(request, user)
            return redirect('Email')
            
        else:
            context['message'] = 'Invalid username/password'
    #update_history(request)        
    return render(request, 'login.html', context)


#SignUp
def signup_view(request):           #SignUp
    update_history(request)

    if request.method == "POST":
        pass

    #update_history(request)
    return HttpResponse('<h1>Hello, World!</h1>Signup')


def email_sender_view(request):     #POST Request Form
    if not request.user.is_authenticated:
        return redirect('Login')

    update_history(request)
    return HttpResponse('<h1>Hello, World!</h1>email_sender')

def logout_view(request):           #Logout
    #update_history(request)
    logout(request)
    return redirect('Home')