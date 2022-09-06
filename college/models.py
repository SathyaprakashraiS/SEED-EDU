from django.db import models

# Create your models here.
class Allcollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	logo=models.ImageField(upload_to='images',default='images/tst2.jpg')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')

class Topcollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')

class Degreecollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')

class Statecollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')

class Citycollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')

class Coursebasedcollege(models.Model):
	name=models.CharField(max_length=200)
	city=models.CharField(max_length=200,default='-')
	state=models.CharField(max_length=200,default='-')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	link=models.CharField(max_length=200,default='#')
	detail=models.CharField(max_length=200,default='UNKNOWN')
	rating=models.CharField(max_length=200,default='NULL')