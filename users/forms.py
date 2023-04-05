from django import forms

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=50, widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label="Password", max_length=65, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Repeat password", max_length=65, widget=forms.PasswordInput, required=True)

    class Meta:
        model = Person
        fields = ['username', 'email', 'password1', 'password2']
