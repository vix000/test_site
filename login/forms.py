import re
from django import forms
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


# class MyForm(forms.Form):
#     myfield = forms.CharField(widget=forms.TextInput(attrs={
#         'class' : 'form-input'}))


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            )
        #one of them /\ \/
        #exclude = ()
