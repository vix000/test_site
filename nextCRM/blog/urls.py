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
    url(r'companies/$', myapp_views.CompaniesView.as_view(), name="companies"),
    url(r'users/$', myapp_views.view_profile, name="view_profile"),
    url(r'users/(?P<pk>\d+)/$', myapp_views.view_profile, name="view_profile_with_pk"),
    url(r'edit_profile/$', myapp_views.edit_profile, name="edit_profile"),
    # url(r'users/(?P<pk>\d+)/edit_profile/$', myapp_views.edit_profile, name="edit_profile_with_pk"),
    url(r'change-password/$', myapp_views.change_password, name="change_password"),
    url(r'^companies/$', myapp_views.CompanyDeleteView.as_view(), name='companies'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', myapp_views.change_friends, name='change_friends'),
    url(r'users/(?P<pk>\d+)/author_confirm_delete/', myapp_views.DeleteUser.as_view(), name='delete_user'),
    url(r'users/(?P<pk>\d+)/user_update/', myapp_views.UpdateUser.as_view(), name='update_user'),
    url(r'companies/(?P<pk>\d+)/company_confirm_delete/', myapp_views.DeleteCompany.as_view(), name='delete_company'),
]
