from django import forms
from .models import BookedService
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookServiceForm(forms.ModelForm):
    class Meta:
        model = BookedService
        fields = ['pet_name', 'service_date', 'additional_notes']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']