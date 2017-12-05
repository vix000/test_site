import re
from django import forms
from login.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="jan_kowalski")), label=_("Username"), error_messages={ 'invalid': _("Only letters, numbers and undescores avaiable.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="example@gmail.com")), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("This username already exists."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Password's didn't match"))
        return self.cleaned_data


class EditProfileForm(UserChangeForm):

    #fill or exclude = in fill gives selected, in exclude excludes selected
    class Meta: #it specifies the metadata for the form itself
        model = User
        fields = (
            'username',
            'email',
            'password' #had to ad the password so that submitting changes would work
            )  




class CompaniesForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = ('post',)