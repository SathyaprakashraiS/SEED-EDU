from django.db import models

# Create your models here.
class Commerce(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Science(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Architecture(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Biology(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Government(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Defence(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Fashiondesign(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Socialscience(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Mathematics(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')

class Postgraduation(models.Model):
	name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
