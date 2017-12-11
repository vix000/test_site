# Create your views here.
#views.py
from login.forms import *


from django.db import models
from django.views.generic import ListView, DetailView, CreateView
from login.models import Post, Friend, CompanyComment
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView
from .forms import CompaniesForm, CommentForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
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
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from login.forms import (
    RegistrationForm,
    EditProfileForm,
    CompaniesForm,
)

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_superuser) #check if the request.user is staff member if yes - allow him to register new users
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

@login_required
def currentUsers(request):
    return render(request, 'users.html')

@login_required
def home(request):
    return render(request,
    'home.html',
    { 'user': request.user }
    )

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get_or_create(pk=pk)
    else:
        user = request.user
    users = User.objects.exclude(pk=request.user.pk)

    # friend = Friend.objects.get(current_user=request.user)
    # friends = friend.users.all() # a list of friends.
    args = {'user': user, 'users': users}
    return render(request, 'users.html', args)

@login_required
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

@login_required
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

class CompaniesView(LoginRequiredMixin, ListView):
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


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('view_profile')


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = '__all__'
    template_name = 'user_update.html'
    success_url = reverse_lazy('view_profile')


class DeleteCompany(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('companies')

class UpdateCompany(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'company_update.html'
    succes_url = reverse_lazy('companies')


class CompanyAdd(LoginRequiredMixin, CreateView):
    form_class = CompaniesForm
    template_name = 'company_form.html'
    success_url = reverse_lazy('companies')


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Post
    fields = '__all__'
    template_name = 'company_details.html'
    success_url = reverse_lazy('companies')

    def get_context_data(self, **kwargs):
        context = super(CompanyDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('company_details', pk=post.pk)
    else:
        form = CommentForm()
    template = 'add_comment.html'
    context = {'form': form}
    return render(request, template, context)



