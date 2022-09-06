from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.
def FAQ(request):
	return render(request,"faq.html",{})

def rnotes(request):
	rnotes=Notes.objects.all()
	context={
		'rnotes':rnotes
	}
	return render(request,"rnotes.html",context)

def readrnotes(request):
	a=request.POST.get('notekey')
	book=Notes.objects.all().filter(pk__exact=a)
	#bookurl=Books.objects.values_list('file').filter(pk__exact=a)
	context={
		'book':book
	}
	return render(request,"readnotes.html",context)

def tips(request):
	tips=Tips.objects.all()
	context={
		'tips':tips
	}
	return render(request,"tips.html",context)

def courses(request):
	course=Onlinecourses.objects.all()
	context={
		'course':course
	}
	return render(request,"onlinecourse.html",context)

def vids(request):
	vids=Videos.objects.all()
	context={
	'vids':vids
	}
	return render(request,"vids.html",context)
