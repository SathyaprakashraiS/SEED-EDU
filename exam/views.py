from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Commerce
from .models import Science
from .models import Architecture
from .models import Defence
from .models import Biology
from .models import Government
from .models import Fashiondesign
from .models import Mathematics
from .models import Socialscience
from .models import Postgraduation

# Create your views here.
def test(request):
	return render(request,"exams.html")

def commerce(request):
	c=Commerce.objects.all()
	return render(request,"commerce.html",{'c':c})

def science(request):
	s=Science.objects.all()
	return render(request,"science.html",{'s':s})

def government(request):
	g=Government.objects.all()
	return render(request,"government.html",{'g':g})

def defence(request):
	d=Defence.objects.all()
	return render(request,"defence.html",{'d':d})

def archietecture(request):
	a=Architecture.objects.all()
	return render(request,"archietecture.html",{'a':a})

def biology(request):
	b=Biology.objects.all()
	return render(request,"biology.html",{'b':b})

def fashiondesign(request):
	f=Fashiondesign.objects.all()
	return render(request,"fashiondesign.html",{'f':f})

def mathematics(request):
	m=Mathematics.objects.all()
	return render(request,"mathematics.html",{'m':m})

def socialscience(request):
	ss=Socialscience.objects.all()
	return render(request,"socialscience.html",{'ss':ss})

def postgrad(request):
	pg=Postgraduation.objects.all()
	return render(request,"postgraduation.html",{'pg':pg})