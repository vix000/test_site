# Create your views here.
#views.py
from login.forms import *

from login.models import Post, Friend
from django.views.generic import TemplateView
from .forms import CompaniesForm
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
    CompaniesForm,
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
 

def currentUsers(request):
    return render(request, 'users.html')

@login_required
def home(request):
    return render(request,
    'home.html',
    { 'user': request.user }
    )

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    users = User.objects.exclude(pk=request.user.pk)
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all() # a list of friends.
    args = {'user': user, 'users': users, 'friends': friends}
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

class CompaniesView(TemplateView):
    template_name = 'companies.html'

    def get(self, request):
        form = CompaniesForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.all()

        args = {'form': form, 'posts': posts, 'users': users}

        return render(request, self.template_name, args)

    def post(self, request):
        form = CompaniesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = CompaniesForm()


        return redirect('/companies')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

class CompanyDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('companies')


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation =='add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('/users')