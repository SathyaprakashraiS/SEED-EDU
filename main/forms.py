from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import *

class CustomUserForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = CustomUser 
        fields ='__all__'

class EditProfileForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = CustomUser
        #fields ='__all__'
        fields =['username','status','standard','hide','img']
        help_texts = {
            'username': None
        }
        #exclude = ['first_name','last_name','password','last_login','superuserstatus','groups','user_permissions','email_address','staff_status','active','date_joined','teacher','Active']