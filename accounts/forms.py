from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'] 

class profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['user','phone_number','image']


