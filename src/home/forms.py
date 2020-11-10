from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm, forms.Form):
    first_name  = forms.CharField(label = "First Name",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "First name",
                                }))
    
    last_name  = forms.CharField(label = "Last Name", required=False,
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Last name",
                                }))
    
    username  = forms.CharField(label = "Username",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "username",
                                }))
    
    email  = forms.CharField(label = "Email",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "xyz@gmail.com",
                                "type"          : "email"
                                }))
    
    password1  = forms.CharField(label = "Password",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Abcd@123",
                                'type'          : 'password'
                                }))
    
    password2  = forms.CharField(label = "Confirm Password",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Abcd@123",
                                'type'          : 'password'
}))

    class Meta:
        model   = User
        fields  = [
            'first_name',
            'last_name',
            'username', 
            'email', 
            'password1', 
            'password2',

        ]

