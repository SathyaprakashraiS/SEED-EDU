from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Qanswersheet(models.Model):
	sname=models.CharField(max_length=200,default='studentname')
	semail=models.CharField(max_length=200,default='studentemail')
	sgrade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
	stest=models.CharField(max_length=200,default='testname')
	spoint=models.CharField(max_length=200,default='0')
	sremark=models.CharField(max_length=500,default='remark')

class MockAnswer(models.Model):
	studentname=models.CharField(max_length=500,default='Stud_0')
	testname=models.CharField(max_length=500,default='sub_0')
	semail=models.CharField(max_length=200,default='studentemail')
	sgrade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
	markobtained=models.IntegerField(default='0')
	totalmarks=models.CharField(max_length=500,default='0')
	answersheet=models.FileField(upload_to='images',default='static/images/default.pdf')
	correctedanswersheet=models.FileField(upload_to='images',default='static/images/default.pdf')
	evaluated=models.BooleanField(default=False)
	evaluatedby=models.CharField(default="ADMIN",max_length=1000)
	tempo=models.IntegerField(default=1)