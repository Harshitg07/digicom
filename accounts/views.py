from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django import forms
from django.contrib.auth.forms import UserCreationForm



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        profile = request.user
        form = SignUpForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            login(request, profile)  
            #return redirect('login')      
    else:
        profile = request.user
    
        form = SignUpForm(initial={'first_name': profile.first_name, 'last_name':profile.last_name, 'email':profile.email, 'username':profile.username, 'password1':profile.password, 'password2':profile.password})
        #form.fields['password1'].widget=forms.HiddenInput()
        #form.fields['password2'].widget=forms.HiddenInput()
        print(profile.password)
    return render(request, 'accounts/profile.html', {'form':form})
