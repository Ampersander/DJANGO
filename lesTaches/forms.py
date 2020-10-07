from django.forms import ModelForm, Textarea
from .models import Task, User
from django import forms
from django.urls import reverse
import datetime


class TaskForm2(ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "closed")


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'scheduled_date','due_date','closed','user')
        widgets = {
            'description': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Entrer votre message ici'}),
            'name': forms.TextInput(attrs={'placeholder': 'Doe'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'firstname', 'email')