from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    
    email  = forms.EmailField(label = "Email",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "xyz@gmail.com",
                                "type"          : "email"
                                }))
    
    password1  = forms.CharField(label = "Password",
                        widget= forms.PasswordInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Abcd@123",
                                }))
    
    password2  = forms.CharField(label = "Confirm Password",
                        widget= forms.PasswordInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Abcd@123",
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
class LoginUserForm(AuthenticationForm):
    
    username  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "login-form-field",
                                "placeholder"   : "username",
                                }))

    
    password  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "login-form-field",
                                "placeholder"   : "Abcd@123",
                                'type'          : 'password'
                                }))
    


    class Meta:
        model   = User
        fields  = [
            'username', 
            'password', 

        ]

