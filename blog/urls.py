"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login import views as myapp_views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth_views.login),
    url(r'^home/$', myapp_views.home),
    url(r'^register/$', myapp_views.register),
    url(r'^register/success/$', myapp_views.register_success),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^logout/$', auth_views.login),
    url(r'companies/$', myapp_views.companies),
    url(r'users/$', myapp_views.currentUsers),
]
