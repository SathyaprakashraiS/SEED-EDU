from django.db import models
import datetime

# Create your models here.

class events(models.Model):
    event_name = models.CharField(max_length=200,default="Some event")
    desc = models.CharField(max_length=300,default="about event")
    Date = models.DateField(default=datetime.date.today)
