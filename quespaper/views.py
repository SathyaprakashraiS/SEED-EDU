from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import QPM,Paper

# Create your views here.
def qpmain(request):
    ptypes=QPM.objects.all()
    return render(request,"newqp.html",{'ptypes':ptypes})
    

def showqp(request):
    a=request.POST.get('paptype')
    # papertype=QPM.objects.values_list('parentpaperfile').filter(pk__exact=a)
    # papertype=str(papertype)[13:-5]
    papers= Paper.objects.filter(childpaperfile=a)
    return render(request,"showqp.html",{'papers':papers})
