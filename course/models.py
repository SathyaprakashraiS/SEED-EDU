from django.db import DefaultConnectionProxy, models

# Create your models here.
class TCourse(models.Model):
	name=models.CharField(max_length=200)
	details=models.CharField(max_length=200)
	link=models.CharField(max_length=200)
	review=models.CharField(max_length=200)
	rating=models.IntegerField(default=0) 

class Art(models.Model):
	name=models.CharField(max_length=200)
	desc = models.CharField(max_length=400,default="about")
	duration = models.IntegerField(default=3)
	img_url = models.URLField(max_length=300,default="https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg")

class Science(models.Model):
	name=models.CharField(max_length=200)
	desc = models.CharField(max_length=400,default="about")
	duration = models.IntegerField(default=3)
	img_url = models.URLField(max_length=300,default="https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg")

class Engineering(models.Model):
	name=models.CharField(max_length=200)
	desc = models.CharField(max_length=400,default="about")
	type = models.CharField(max_length=10,default="BTECH")
	duration = models.IntegerField(default=4)
	img_url = models.URLField(max_length=300,default="https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg")

class Commerce(models.Model):
	name=models.CharField(max_length=200)
	desc = models.CharField(max_length=400,default="about")
	duration = models.IntegerField(default=3)
	img_url = models.URLField(max_length=300,default="https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg")
	
class Professional(models.Model):
	name=models.CharField(max_length=200)
	desc = models.CharField(max_length=400,default="about")
	duration = models.IntegerField(default=2)
	img_url = models.URLField(max_length=300,default="https://images.hindustantimes.com/rf/image_size_640x362/HT/p2/2015/12/01/Pictures/_c34102da-9849-11e5-b4f4-1b7a09ed2cea.jpg")