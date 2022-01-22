from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class QPM(models.Model):
    parentpaperfile= models.CharField(max_length=200)
    forgrade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
    description = models.CharField(max_length=100,default="The description")

    def __str__(self):
        return "%s" % (self.parentpaperfile)

class Paper(models.Model):
    childpaperfile= models.ForeignKey(QPM,on_delete=models.CASCADE)#nothing but ask which board what what subject is the qp realted to 
    name=models.CharField(max_length=200)
    forgrade=models.IntegerField(default=10,validators=[MaxValueValidator(12), MinValueValidator(10)])
    papertype=models.CharField(max_length=200,default='Practise papeR')
    key=models.CharField(max_length=200,default='VieW')
    year=models.CharField(max_length=200,default='UnknowN')
    paper=models.FileField(upload_to='images',default='images/none.pdf')
    addedby=models.CharField(max_length=1000,default="ADMIN")
    visible=models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

