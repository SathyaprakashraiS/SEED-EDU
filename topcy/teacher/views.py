from django.db.models import fields
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, request
from .forms import *
from student.models import MockAnswer 
from django.views.decorators.cache import cache_control
from .models import *
from django.views.generic.edit import UpdateView

# Create your views here.
def home(request):
	return render(request,"teacherhome.html",{})

def addcourse(request):
	if request.method == 'POST':
		form = AddtestnameT(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'addcourse.html', {'form': form})
	else:
		form = AddtestnameT()
	return render(request, 'addcourse.html', {'form': form})

def addquestion(request):
	if request.method == 'POST':
		form = AddquestionT(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'addquestion.html', {'form': form})
	else:
		form = AddquestionT()
	return render(request, 'addquestion.html', {'form': form})

def asses(request):
	tgrade=request.user.standard
	papers=MockAnswer.objects.all().filter(sgrade=tgrade)
	epapers=Assesedanswer.objects.all()
	for i in epapers:
		for j in papers:
			if str(i.testname)==str(j.testname):
				papers=papers.exclude(testname=i.testname)
	context={
		'papers':papers,'epapers':epapers
	}
	return render(request,"asses.html",context)

@cache_control(no_cache=True, must_revalidate=False, no_store=True)
def assespaper(request):
	form =CorrectedpaperForm(request.POST, request.FILES)
	q=request.POST.get('testname')
	paper=MockAnswer.objects.all().filter(pk__exact=q)

	if request.method == 'POST':
		if form.is_valid():
			print("enga illa eruken murugesa")
			form.save()
	context={
	'paper':paper,'form':form,'q':q
	}
	return render(request,"assespaper.html",context)

def saveassespaper(request):
	if request.method == 'POST':
		form = CorrectedpaperForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			img_obj = form.instance
			return redirect('/teacher/')
		else:
			print(form.errors)
			return redirect('/teacher/')

#module not done
def checkpaper(request):
	theid=request.POST.get("testname")
	paper=Assesedanswer.objects.all().filter(pk__exact=theid)
	mafilterkey=Assesedanswer.objects.values_list('key').filter(pk__exact=theid)
	mafilterkey=str(mafilterkey)[13:-5]
	studpaper=MockAnswer.objects.all().filter(pk__exact=mafilterkey)
	context={
		'paper':paper,'studpaper':studpaper
	}
	return render(request,"checkpaper.html",context)

def addquiz(request):
	qform =AddquizForm(request.POST, request.FILES)
	qqform=AddquizquestionForm()
	delquiz=AddquizT.objects.all()
	context={
	'qform':qform,'qqform':qqform,'delquiz':delquiz
	}
	return render(request,"modquiz.html",context)

def createaddquiz(request):
	form =AddquizForm(request.POST, request.FILES)
	if request.method == 'POST':
		form = AddquizForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/teacher/QCRUD/')
		else:
			print(form.errors)
			return redirect('/teacher/QCRUD/')

def addquizques(request):
	form =AddquizquestionForm(request.POST, request.FILES)
	if request.method == 'POST':
		form = AddquizquestionForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/teacher/QCRUD/')
		else:
			print(form.errors)
			return redirect('/teacher/QCRUD/')

def delquiz(request):
	a=request.POST.get('quizkey')
	AddquizT.objects.filter(pk__exact=a).delete()
	return redirect('/teacher/QCRUD/')

def delques(request):
	a=request.POST.get('quizkey')
	quiz=AddquizT.objects.values_list('cname').filter(pk__exact=a)
	# for i in quiz:
	# 	i.quiz=str(i.quiz)[13:-5]
	quiz=str(quiz)[13:-5]
	questions=AddquestionT.objects.all().filter(testgrade=a)
	# for i in quiz:
	# 	questions=AddquestionT.objects.all().filter(testgrade=i.quiz)
	context={
	'quiz':quiz,'questions':questions
	}
	return render(request,"delques.html",context)

def delquizques(request):
	a=request.POST.get('delqueskey')
	AddquestionT.objects.filter(pk__exact=a).delete()
	return redirect('/teacher/QCRUD/')

def ECRUD(request):
	cmockform=MockPMForm()
	usergrade=request.user.standard
	mockexams=MockPM.objects.all().filter(mpgrade=usergrade)
	context={
		'cmockform':cmockform,'mockexams':mockexams
	}
	return render(request,"ecrud.html",context)

def addexam(request):
	if request.method == 'POST':
		form = MockPMForm(request.POST, request.FILES)
		img_obj = form.instance
		if form.is_valid():
			form.save()
			return redirect('/teacher/ECRUD/')
		else:
			print(form.errors)
			return redirect('/teacher/')

def delexam(request):
	a=request.POST.get('mocktestid')
	examname=MockPM.objects.values_list('mockpapername').filter(pk__exact=a)
	MockPM.objects.all().filter(pk__exact=a).delete()
	examname=str(examname)[13:-5]
	Assesedanswer.objects.all().filter(testname=examname).delete()
	MockAnswer.objects.all().filter(testname=examname).delete()
	return redirect('/teacher/ECRUD/')

class updateMock(UpdateView):
	model = MockPM
	fields = "__all__"
	template_name = 'modexam.html'
	success_url="/teacher/ECRUD/"
# def modexam(request):
# 	a=request.POST.get('modtestid') 
# 	q=request.POST.get('q')
# 	if(q):
# 		if request.method == 'POST':
# 			form = MockPMForm(request.POST, request.FILES,instance=a)
# 			if form.is_valid():
# 				form.save()
# 				return redirect('/teacher/')
# 			return redirect('/teacher/ECRUD/')

# 	else:
# 		form = MockPMForm(request.POST, request.FILES)
# 		return render(request,"modexam.html",{})

