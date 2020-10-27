from django.shortcuts import (redirect, render,  )
from django.http import (HttpResponse, )

#User and login imports
from django.contrib.auth import authenticate, login, logout

#created module
from .extra import (
    create_user_,
    update_history,
)

def home_view(request):             #
    update_history(request)
    context = {
        
    }
    return render(request, 'index.html', context)
    

#Login and Logout
def login_view(request):            #Login
    update_history(request)

    if request.method == "POST":
        username_   = request.POST.get('username')
        password_   = request.POST.get('password')

        print(username_,password_)
        user = authenticate(username = username_, password = password_)
        login(request, user)
        return redirect('../')
        if user is not None:
            login(request, user)
            return redirect('../')
            

        else:
            pass
            # Warning/ReCheck Message
    
    context = {
        
    }
    return render(request, 'login.html', context)


#SignUp
def signup_view(request):           #SignUp
    update_history(request)

    if request.method == "POST":
        pass

    return HttpResponse('<h1>Hello, World!</h1>Signup')


def email_sender_view(request):     #POST Request Form
    update_history(request)
    return HttpResponse('<h1>Hello, World!</h1>email_sender')