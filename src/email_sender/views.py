from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from.forms import EmailForm

def index(request):
    form = EmailForm()
    if request.user.is_anonymous:
        return redirect('Home:Home')

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            #send mail
            print("Mail Sent")
            print(form.cleaned_data)



    context = {
        'form' : form,
    }
    return render(request, 'email_sender/textarea.html', context)