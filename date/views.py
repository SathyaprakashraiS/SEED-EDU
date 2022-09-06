from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def date(request):
	obj = events.objects.filter().order_by('Date')
	return render(request,"date.html",{"obj":obj})