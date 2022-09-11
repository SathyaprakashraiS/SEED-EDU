from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
 
# Create your views here.
def chome(request):
	return render(request,"communities.html")
def cten(request):
	#a=Art.objects.all()
	#return render(request,"carts.html",{'a':a})
	return render(request,"communityten.html",{})