from django.db import models
from seededu import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):
	name=models.CharField(max_length=200)
	liner=models.CharField(max_length=400,default='2 line info about it')
	date=models.CharField(max_length=200,default='00-MON, 0000')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	url=models.CharField(max_length=200,default='#')

User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    teacher=models.BooleanField(default=False)
    status=models.CharField(max_length=25,default='Studying...') 
    remark=models.CharField(max_length=100,default='NA')
    standard=models.IntegerField(default=10)
    hide=models.BooleanField(default=False)
    img=models.ImageField(upload_to='images',default='images/profpic.jpeg')

class Dialogues(models.Model):
	thought=models.CharField(max_length=250)
	approval=models.BooleanField(default=False)
	author=models.CharField(max_length=100)