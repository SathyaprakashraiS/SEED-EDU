from django.db import models

# Create your models here.
class Community(models.Model):
	commname=models.CharField(max_length=200,default='commname')
	commicon=models.ImageField(default="images/tst2.jpg")
	comgrade=models.CharField(max_length=200,default='commgrade')
	commcreatedby=models.CharField(max_length=200,default='createdby')
	visibility=models.BooleanField(default=True)

class Chat(models.Model):
	communitytype=models.ForeignKey(Community,on_delete=models.CASCADE)
	comment=models.CharField(max_length=200,default='message')
	madeby=models.CharField(max_length=200,default='sender')
	madebymail=models.CharField(max_length=200,default='sendermail')
	visibility=models.BooleanField(default=True)

	def __str__(self):
		return self.madebymail

	class Meta:
		ordering = ['communitytype']