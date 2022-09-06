from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Allcollege
from .models import Topcollege
from .models import Degreecollege
from .models import Statecollege
from .models import Citycollege
from .models import Coursebasedcollege

# Create your views here.
def college(request):
	return render(request,"college.html")

def allcollege(request):
	a=Allcollege.objects.all()
	return render(request,"allcollege.html",{'a':a})

def topcollege(request):
	t=Topcollege.objects.all()
	return render(request,"topcollege.html",{'t':t})

def degreebasedcollege(request):
	d=Degreecollege.objects.all()
	return render(request,"degreebasedcollege.html",{'d':d})

def statebasedcollege(request):
	s=Allcollege.objects.filter(state="Tamil Nadu")
	return render(request,"statebasedcollege.html",{'s':s})


def citybasedcollege(request):
	c=Citycollege.objects.all()
	return render(request,"citybasedcollege.html",{'c':c})

def coursebasedcollege(request):
	co=Coursebasedcollege.objects.all()
	return render(request,"coursebasedcollege.html",{'co':co})
#def test(request):
#	return render(request,"exams.html")
 