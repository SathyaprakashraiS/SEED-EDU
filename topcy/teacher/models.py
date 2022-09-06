from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Course -> SUBJECT

class AddquizT(models.Model):
	cname=models.CharField(max_length=200,default='quiz_name')
	author=models.CharField(max_length=200,default='teacher_name')
	cgrade=models.IntegerField(default=10)

	def __str__(self):
		return self.cname

class AddquestionT(models.Model):
	testgrade=models.ForeignKey(AddquizT,on_delete=models.CASCADE)
	cquestion=models.CharField(max_length=500,default='Question')
	coption1=models.CharField(max_length=500,default='Option1')
	coption2=models.CharField(max_length=500,default='Option2')
	coption3=models.CharField(max_length=500,default='Option3')
	coption4=models.CharField(max_length=500,default='Option4')
	canswer=models.IntegerField(default=1,validators=[MaxValueValidator(4), MinValueValidator(1)])

	def __str__(self):
		return self.cquestion

	class Meta:
		ordering = ['cquestion']

class QuizAnswer(models.Model):
	studentname=models.CharField(max_length=500,default='Stud_0')
	subname=models.CharField(max_length=500,default='sub_0')
	grade=models.CharField(max_length=500,default='10')
	markobtained=models.CharField(max_length=500,default='0')
	totalmarks=models.CharField(max_length=500,default='0')

class MockPM(models.Model):
    mockpapername= models.CharField(max_length=200)
    paperdescription= models.CharField(max_length=100,default="The description")
    mpgrade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
    mockpaper=models.FileField(upload_to='images')
    totalmarks=models.IntegerField(default=0)

class Assesedanswer(models.Model):
	key=models.CharField(max_length=10,default="id")
	studentname=models.CharField(max_length=500,default='Stud_0')
	testname=models.CharField(max_length=500,default='sub_0')
	semail=models.CharField(max_length=200,default='studentemail')
	correctedanswersheet=models.FileField(upload_to='images',default='static/images/default.pdf')
	markobtained=models.IntegerField(default=0)
	evaluated=models.BooleanField(default=True)
#class MockAnswer(models.Model):
#	studentname=models.CharField(max_length=500,default='Stud_0')
#	testname=models.CharField(max_length=500,default='sub_0')
#	grade=models.IntegerField()
#	markobtained=models.CharField(max_length=500,default='0')
#	totalmarks=models.CharField(max_length=500,default='0')
#	answersheet=models.FileField(upload_to='images')