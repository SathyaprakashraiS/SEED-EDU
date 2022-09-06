from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class BookTypes(models.Model):
    forgrade= models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
    def __str__(self):
        return "%s" % (self.forgrade)

class Books(models.Model):
    bgrade=models.ForeignKey(BookTypes,on_delete=models.CASCADE)
    #bgrade=models.IntegerField(default=10)
    name=models.CharField(max_length=200,default='book name')
    subject=models.CharField(max_length=200,default="10science,11maths,12english,Main,Neet...")
    details=models.CharField(max_length=200,default='details unavailable')
    review=models.CharField(max_length=200,default='book review')
    rating=models.FloatField(default=0)
    image=models.ImageField(default="images/tst2.jpg")
    author=models.CharField(max_length=200,default="NCERT")
    file=models.FileField(default="images/default.pdf")
    addedby=models.CharField(max_length=1000,default="Admin")
    visible=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Twelve(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf')

class Eleven(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf') 

class Ten(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf')

class Neet(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf')

class Jeemain(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf') 

class Jeeadvance(models.Model):
	name=models.CharField(max_length=200)
	url=models.CharField(max_length=200,default='#')
	img=models.ImageField(upload_to='images',default='images/tst2.jpg')
	#book=models.FileField(upload_to='images', default='images/none.pdf')