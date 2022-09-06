from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import *
from django.contrib.auth import get_user_model
from student.models import MockAnswer

class AddquizForm(forms.ModelForm):
	"""Form for the image model"""
	class Meta:
		model = AddquizT
		fields = '__all__'
		
class AddquizquestionForm(forms.ModelForm):
	"""Form for the image model"""
	class Meta:
		model = AddquestionT
		#fields = ["testgrade","cquestion","coption1","coption2","coption3","coption4","canswer"]
		fields= '__all__'
 
class MockPMForm(forms.ModelForm):
	"""Form for the image model"""
	class Meta:
		model = MockPM
		#fields = ['mockpapername','paperdescription','mpgrade','mockpaper']
		fields= '__all__'

class CorrectedpaperForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
       model = Assesedanswer
       fields= '__all__'
       #fields=['correctedanswersheet']
       #fields = ['studentname','testname','semail','sgrade','markobtained','totalmarks','answersheet','correctedanswersheet','evaluated']

