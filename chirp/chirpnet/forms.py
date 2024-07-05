from django import forms
from .models import ChirpNet

class ChirpNetForm(forms.ModelForm):
    # imp - syntax for creating a new form (Meta)
    class Meta:    
        model=ChirpNet
        fields = ['text', 'photo']