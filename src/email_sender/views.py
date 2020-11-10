from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User


def index(request):
    if request.user.is_anonymous:
        return redirect('Home:Home')


    return render(request, 'email_sender/textarea.html')