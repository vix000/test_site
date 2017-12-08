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
from login import views as myapp_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'post'

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth_views.login),
    url(r'^home/$', myapp_views.home, name="home"),
    url(r'^register/$', myapp_views.register, name='register'),
    url(r'^add_company/$', myapp_views.CompanyAdd.as_view(), name='add_company'),
    url(r'companies/(?P<pk>\d+)/comment_company/$', myapp_views.CompanyComment.as_view(), name='comment_company'),
    # url(r'companies/(?P<article_id>[0-9]+)/comment_company$', myapp_views.add_comment, name='add_comment'),
    url(r'^register/success/$', myapp_views.register_success),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'companies/$', myapp_views.CompaniesView.as_view(), name="companies"),
    url(r'users/$', myapp_views.view_profile, name="view_profile"),
    url(r'edit_profile/$', myapp_views.edit_profile, name="edit_profile"),
    url(r'change-password/$', myapp_views.change_password, name="change_password"),
    url(r'^companies/$', myapp_views.CompanyDeleteView.as_view(), name='companies'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', myapp_views.change_friends, name='change_friends'),
    url(r'users/(?P<pk>\d+)/author_confirm_delete/', myapp_views.DeleteUser.as_view(), name='delete_user'),
    url(r'users/(?P<pk>\d+)/user_update/', myapp_views.UpdateUser.as_view(), name='update_user'),
    url(r'companies/(?P<pk>\d+)/company_confirm_delete/', myapp_views.DeleteCompany.as_view(), name='delete_company'),
    url(r'companies/(?P<pk>\d+)/company_update/', myapp_views.UpdateCompany.as_view(), name="edit_company"),
    url(r'companies/(?P<pk>\d+)/company_details/', myapp_views.CompanyDetail.as_view(), name="company_details"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
