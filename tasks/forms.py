from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Task

class TaskForm(forms.ModelForm):
    IMPORTANCE_CHOICES = [
        (False, 'Normal'),
        (True, 'Alta')
    ]

    importante = forms.ChoiceField(choices=IMPORTANCE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'importante']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre de usuario'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña' 
    })) 