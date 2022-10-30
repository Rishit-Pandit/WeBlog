from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    handle = forms.CharField(max_length=100)
    dob = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'handle', 'email', 'dob', 'password1', 'password2']
