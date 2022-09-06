from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import get_user_model

class MockAnswerForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = MockAnswer
       fields = ['studentname','semail','sgrade','testname','totalmarks','answersheet']
