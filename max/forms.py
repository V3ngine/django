from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Login'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Rep.password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Login', widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Login'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password'}))