from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Username'}))
    email = forms.EmailField(widget= forms.EmailInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Username'}))
    password1 = forms.CharField(label='Password',widget= forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Password'}))
    password2 = forms.CharField(label='Confirm Password',widget= forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Username'}))
    password = forms.CharField(widget= forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Password'}))
    
class ProfileUpdateForm(forms.ModelForm):
    # name = forms.CharField(widget= forms.TextInput(
    #     attrs={'class' : 'form-control',
    #            'placeholder': 'Input Username'}))
    # gender = forms.CharField(widget= forms.TextInput(
    #     attrs={'class' : 'form-control',
    #            'placeholder': 'Input Username'}))
    # age = forms.IntegerField(widget= forms.NumberInput(
    #     attrs={'class' : 'form-control',
    #            'placeholder': 'Input Username'}))
    # height = forms.IntegerField(widget= forms.NumberInput(
    #     attrs={'class' : 'form-control',
    #            'placeholder': 'Input Username'}))
    # weight = forms.IntegerField(widget= forms.NumberInput(
    #     attrs={'class' : 'form-control',
    #            'placeholder': 'Input Username'}))
    
    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ['user','BMR']

class calloryForm(forms.ModelForm):
    class Meta:
        model=callory
        fields = ('__all__')
        exclude = ['user']