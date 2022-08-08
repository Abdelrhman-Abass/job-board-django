from django.urls import reverse
from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from django.shortcuts import render ,redirect
from .forms import *
from django.contrib.auth import authenticate ,login
from .models import profile 
# Create your views here.

def signup(request):

    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/Profile')
    
    else:
        form = signup_form()
    return render(request, 'registration\signup.html', {'form':form})

def Profile(request):
    Profile = profile.objects.get(user=request.user)
    return render(request, 'account/profile.html', {'profile': Profile})


    

def profile_edit(request):
    Profile = profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = user_form(request.POST,instance=request.user)
        profileform = profile_form(request.POST,request.FILES,instance=Profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:Profile'))
    else:
        userform = user_form(instance=request.user)
        profileform = profile_form(instance=Profile)
    return render(request, 'account/profile_edit.html', {'userform': userform , 'profileform': profileform})