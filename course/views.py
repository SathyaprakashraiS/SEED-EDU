from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Art
from .models import Science
from .models import Commerce
from .models import Engineering
from .models import Professional
 
# Create your views here.
def courses(request):
	return render(request,"course.html")
def arts(request):
	a=Art.objects.all()
	return render(request,"carts.html",{'a':a})
def science(request):
	s=Science.objects.all()
	return render(request,"cscience.html",{'s':s})
def commerce(request):
	c=Commerce.objects.all()
	return render(request,"ccommerce.html",{'c':c})
def engineering(request):
	e=Engineering.objects.all()
	return render(request,"cengineering.html",{'e':e})
def procourse(request):
	p=Professional.objects.all()
	return render(request,"cpro.html",{'p':p})