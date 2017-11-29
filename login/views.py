# Create your views here.
#views.py
from login.forms import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash # to remain logged in after changing password
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login.forms import (
    RegistrationForm,
    EditProfileForm,
)
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = {
    'form': form
    }
 
    return render(request, 'registration/register.html' ,variables)
 
def register_success(request):
    return render(request,
    'registration/success.html',)
 
def logout_page(request):
    logout(request)
    return render(request, '/')
 
def companies(request):
    return render(request,
     'companies.html',)

def currentUsers(request):
    return render(request, 'users.html')

@login_required
def home(request):
    return render(request,
    'home.html',
    { 'user': request.user }
    )

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'users.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/users')

    else:
        form = EditProfileForm(instance=request.user)
        args={'form': form}
        return render(request, 'edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/users')
        else:
            return redirect('/change-password')  #if form.is_valid() == False -> if user inputted wrong data

    else:
        form = PasswordChangeForm(user=request.user)
        args={'form': form}
        return render(request, 'change_password.html', args)