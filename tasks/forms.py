from django import forms
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
