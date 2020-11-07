from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    first_name  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "First name",
                                }))
    
    last_name  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Last name",
                                }))
    
    username  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "username",
                                }))
    
    email  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "xyz@gmail.com",
                                }))
    
    password1  = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {
                                "class"         : "form-control",
                                "placeholder"   : "Abcd@123",
                                }))
    
    password2  = forms.CharField(label = "",
                        widget= forms.TextInput(
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

'''class ProductForm(forms.ModelForm):
    title       = forms.CharField(label = "",
                        widget= forms.TextInput(
                            attrs = {"placeholder":"Product Name",}))

    price       = forms.DecimalField(initial=None, label="",
                        widget= forms.NumberInput(
                            attrs = {"placeholder":"Product Price",}))

    description = forms.CharField(label = "",
                        required = False,
                        widget= forms.Textarea(
                            attrs = {
                                "placeholder":"Product Description",
                                "rows":25,
                                'cols':100,
                                
                                }))

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            
        ]

    '''