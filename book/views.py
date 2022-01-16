from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def books(request):
	obj=Books.objects.all()
	return render(request,"library.html",{'obj':obj})

def viewbook(request):
	a=request.POST.get('bname')
	obj=Books.objects.filter(btype__booktype=a)
	return render(request,"thebook.html",{'obj':obj})

'''
def books(request):
	return render(request,"library.html")
'''

def twelth(request):
	tw=Twelve.objects.all()
	return render(request,"twelve.html",{'tw':tw})

def eleventh(request):
	el=Eleven.objects.all()
	return render(request,"eleven.html",{'el':el})

def tenth(request):
	te=Ten.objects.all()
	return render(request,"ten.html",{'te':te})

def neet(request):
	n=Neet.objects.all()
	return render(request,"neet.html",{'n':n})

def jeemain(request):
	jm=Jeemain.objects.all()
	return render(request,"jeemain.html",{'jm':jm})

def jeeadvance(request):
	ja=Jeeadvance.objects.all()
	return render(request,"jeeadvance.html",{'ja':ja})