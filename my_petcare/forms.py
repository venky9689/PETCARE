from django import forms
from .models import BookedService

class BookServiceForm(forms.ModelForm):
    class Meta:
        model = BookedService
        fields = ['pet_name', 'service_date', 'additional_notes']
        
        
        

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']