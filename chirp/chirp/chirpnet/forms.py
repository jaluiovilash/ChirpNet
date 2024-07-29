from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ChirpNet

class ChirpNetForm(forms.ModelForm):
    # imp - syntax for creating a new form (Meta)
    class Meta:    
        model=ChirpNet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')