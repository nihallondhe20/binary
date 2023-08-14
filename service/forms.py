from django import forms
from .models import User
from django.forms import TextInput, EmailInput
from . models import Service
import datetime

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname','lastnamr','phone','comments','service_type','status']
       
        

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'service_name': forms.TextInput(attrs={'label':'Service game','class': 'form-control','placeholder': 'green','margin':'10px'}),
              'service_type': forms.TextInput(attrs={'class': 'form-control',})
        }