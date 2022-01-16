from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from teacher.models import *
from book.models import *
from .models import *
from .forms import *
from main.models import *
from book.models import Books
from django.views.decorators.cache import cache_control
from django.shortcuts import redirect

# Create your views here.

def home(request):
	usermail=request.user.email
	MockAnswer.objects.filter(testname="",semail=usermail).delete()
	Qanswersheet.objects.filter(stest="",semail=usermail).delete()
	usermail=request.user.email
	standard=request.user.standard
	qans=Qanswersheet.objects.all().filter(sgrade=standard)
	quiz10=AddquizT.objects.all().filter(cgrade=10)
	quiz11=AddquizT.objects.all().filter(cgrade=11)
	quiz12=AddquizT.objects.all().filter(cgrade=12)
	mt10=MockPM.objects.all().filter(mpgrade=10)
	mt11=MockPM.objects.all().filter(mpgrade=11)
	mt12=MockPM.objects.all().filter(mpgrade=12)
	mans=MockAnswer.objects.all().filter(sgrade=standard)
	thoughts=Dialogues.objects.all()
	for i in qans:
		if i.semail==usermail:
			quiz10=quiz10.exclude(cname=i.stest)
			quiz11=quiz11.exclude(cname=i.stest)
			quiz12=quiz12.exclude(cname=i.stest)
	for i in mans:
		if i.semail==usermail:
			mt10=mt10.exclude(mockpapername=i.testname)
			mt11=mt11.exclude(mockpapername=i.testname)
			mt12=mt12.exclude(mockpapername=i.testname)
	book10=Books.objects.all().filter(bgrade__forgrade=10)
	book11=Books.objects.all().filter(bgrade__forgrade=11)
	book12=Books.objects.all().filter(bgrade__forgrade=12)
	qa=Qanswersheet.objects.all().filter(semail=usermail)
	ma=MockAnswer.objects.all().filter(semail=usermail,evaluated=True)
	mae=MockAnswer.objects.all().filter(semail=usermail)
	context={
		"quiz10":quiz10,"quiz11":quiz11,"quiz12":quiz12,"book10":book10,"book11":book11,"book12":book12,'qa':qa,'mt10':mt10,
		'mt11':mt11,'mt12':mt12,'ma':ma,'thoughts':thoughts,'mae':mae
	}
	return render(request,"studenthome.html",context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def quiz(request):
	done=0
	usermail=request.user.email
	qans=Qanswersheet.objects.all()
	a=request.POST.get('custom')
	testname=AddquizT.objects.values_list('cname').filter(pk__exact=a)
	temptestname=str(testname)[13:-5]

	score=0
	wrong=0
	correct=0
	total=0
	name=request.user.username
	mail=request.user.email
	standard=request.user.standard
	donealready=Qanswersheet.objects.all().filter(sname=name,stest=temptestname)
	deleted=Qanswersheet.objects.all().filter(sname=name,stest=" ")
	
	if donealready:
		return redirect('/student/')
	elif deleted:
		return redirect('/student/')
	else:
		Qanswersheet.objects.create(sname=name,semail=mail,sgrade=standard,stest=temptestname,spoint=score)

	for i in qans:
		if i.semail==usermail and i.stest==temptestname:
			done=1
	paper=AddquestionT.objects.all().filter(testgrade=a)
	ans=AddquestionT.objects.values_list('canswer').filter(testgrade=a)
	key=a
	return render(request,'quiz.html',{'testname':testname,'paper':paper,'key':key,'done':done})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def quizresult(request):
	if request.method == 'POST':
		b=request.POST.get('subname')
		theb=AddquizT.objects.values_list('cname').filter(pk__exact=b)
		#print("this is b: ",str(theb)[13:-5])
		theb=str(theb)[13:-5]
		#print("the modified theb is :",theb)
		ans=AddquestionT.objects.values_list('canswer').filter(testgrade=b)
		questions=AddquestionT.objects.all().filter(testgrade=b)
		score=0
		wrong=0
		correct=0
		total=0
		for q in questions:
			total+=1
			#print(request.POST.get(q.cquestion))
			#print(q.canswer)
			#print()
			if str(q.canswer) ==  str(request.POST.get(q.cquestion)):
				#print("potachu marku")
				score+=10
				correct+=1
			else:
				#print("thappu poten :)")
				wrong+=1
		percent=(score/(total*10))/100
		name=request.user.username
		mail=request.user.email
		standard=request.user.standard
		#Qanswersheet.objects.create(sname=name,semail=mail,sgrade=standard,stest=theb,spoint=score)
		Qanswersheet.objects.filter(sname=name,stest=theb).update(sname=name,semail=mail,sgrade=standard,stest=theb,spoint=score)
		#QuizAnswer.objects.create(studentname=,subname=,grade=,marksobtained=,totalmarks=)
		context ={'score':score,'correct':correct,'wrong':wrong,'percent':percent,'total':total}
		return render(request,'quizmarker.html',context)

def quizans(request):
	key=request.POST.get('key')
	viewable=AddquestionT.objects.all().filter(testgrade__cname=key)
	ansopt=AddquestionT.objects.values_list('canswer').filter(testgrade__cname=key)
	return render(request,"quizans.html",{'viewable':viewable,'ansopt':ansopt})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mockexam(request):
	usermail=request.user.email
	name=request.user.username
	standard=request.user.standard
	b=request.POST.get('mockname')
	tname=MockPM.objects.values_list('mockpapername').filter(pk__exact=b)
	tname=str(tname)[13:-5]
	thep=MockPM.objects.all().filter(pk__exact=b)
	if request.method == 'POST':
		b=request.POST.get('mockname')
		thep=MockPM.objects.all().filter(pk__exact=b)
		attended=MockAnswer.objects.all().filter(semail=usermail,testname=tname)
		if attended:
			return redirect('/student/')
		else:
			MockAnswer.objects.create(studentname=name,semail=usermail,sgrade=standard,testname=tname,tempo=69)

		form = MockAnswerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			MockAnswer.objects.filter(tempo=69,semail=usermail).delete()
			img_obj = form.instance
			return redirect('/student/')

	#answer upload facility
	#if request.method == 'POST':
	context={
		'thep':thep,'form':form
	}
	'''attended=MockAnswer.objects.all().filter(semail=usermail,testname=b)
	if attended:
		return redirect('/student/')
	else:'''
	return render (request,"mockexam.html",context)

def book(request):
	a=request.POST.get('bookkey')
	book=Books.objects.all().filter(pk__exact=a)
	#bookurl=Books.objects.values_list('file').filter(pk__exact=a)
	context={
		'book':book
	}
	return render(request,"book.html",context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def quizwarner(request):
	usermail=request.user.email
	b=request.POST.get('custom')
	qno=AddquestionT.objects.all().filter(testgrade=b)
	theb=AddquizT.objects.values_list('cname').filter(pk__exact=b)
	theb=str(theb)[13:-5]
	context={
		'b':b,'theb':theb,'qno':qno
	}
	return render(request,"quizwarning.html",context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mockwarner(request):
	usermail=request.user.email
	b=request.POST.get('mockname')
	theb=MockPM.objects.values_list('mockpapername').filter(pk__exact=b)
	theb=str(theb)[13:-5]
	context={
		'b':b,'theb':theb
	}
	return render(request,"mockwarning.html",context)