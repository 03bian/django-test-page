from django import forms
from django.contrib.auth.models import User
from .models import UserBasicInfoModels

class UserBasicInfoForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields = ('username', 'email', 'password')


class UserAdditionalInfoForm(forms.ModelForm):
    class Meta():
        model = UserBasicInfoModels
        fields = ('portfolio_site', 'profile_pic')
