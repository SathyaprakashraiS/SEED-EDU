from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from book.models import Books
from college.models import Allcollege
from quespaper.models import *
from .serializers import *
from date.models import *
from course.models import *
from other.models import *
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User


user = settings.AUTH_USER_MODEL
#Create your views here.

class GoogleLogin(SocialLoginView):
	adapter_class = GoogleOAuth2Adapter

def home(request):
	return render(request,"home.html",{})

def news(request):
	n=News.objects.all()
	return render(request,"news.html",{'n':n})

def game(request):
	return render(request,"gametest.html",{})
#def test(request):
#	return render(request,"exams.html")

'''
def edit(request):
	return render(request,"editprofile.html",{})
'''

def view(request):
	obj=CustomUser.objects.all()
	return render(request,"viewprofile.html",{'obj':obj})

def edit(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES,instance=request.user)
		if form.is_valid():
			form.save()
			#img_obj = form.instance
			#return render(request,"editprofile.html", {'form': form, 'img_obj': img_obj})
			return render(request,"editprofile.html", {'form': form})
	else:
		form = EditProfileForm(instance=request.user)
	return render(request,"editprofile.html", {'form': form}) 

#API
@api_view(['GET'])
def Abooklist(request):
	books = Books.objects.all().order_by('-id')
	serializer = BookSerializer(books, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Anewslist(request):
	news = News.objects.all().order_by('-id')
	serializer = NewsSerializer(news, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aallcollegelist(request):
	allcol = Allcollege.objects.all().order_by('-id')
	serializer = AcollegeSerializer(allcol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Atopcollegelist(request):
	topcol = Topcollege.objects.all().order_by('-id')
	serializer = TcollegeSerializer(topcol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Adegreecollegelist(request):
	degcol = Degreecollege.objects.all().order_by('-id')
	serializer = DcollegeSerializer(degcol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Astatecollegelist(request):
	stacol = Allcollege.objects.filter(state="Tamil Nadu").order_by('-id')
	serializer = ScollegeSerializer(stacol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Acitycollegelist(request):
	citycol = Citycollege.objects.all().order_by('-id')
	serializer = CcollegeSerializer(citycol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Acoursecollegelist(request):
	coursecol = Coursebasedcollege.objects.all().order_by('-id')
	serializer = CbcollegeSerializer(coursecol, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Apaperlist(request):
	papers = Paper.objects.all().order_by('-id')
	serializer = PaperSerializer(papers, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Auserslist(request):
	theuser = CustomUser.objects.all().order_by('-id')
	serializer = UserSerializer(theuser, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aartscourselist(request):
	artlist = Art.objects.all().order_by('-id')
	serializer = ArtSerializer(artlist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Asciencecourselist(request):
	sciencelist = Science.objects.all().order_by('-id')
	serializer = ScienceSerializer(sciencelist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aengineeringcourselist(request):
	englist = Engineering.objects.all().order_by('-id')
	serializer = EngineeringSerializer(englist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Acommercecourselist(request):
	commslist = Commerce.objects.all().order_by('-id')
	serializer = CommerceSerializer(commslist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aprofessionalcourselist(request):
	proflist = Professional.objects.all().order_by('-id')
	serializer = ProcourseSerializer(proflist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Adateslist(request):
	datelist = events.objects.all()
	serializer = DateSerializer(datelist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquestionbanktypeslist(request):
	qpbanklist = QPM.objects.all()
	serializer = QPbankSerializer(qpbanklist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquestionbanklist(request,key):
	qplist=Paper.objects.filter(childpaperfile=key)
	serializer = QpapersSerializer(qplist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arnoteslist(request):
	noteslist=Notes.objects.all()
	serializer = NotesSerializer(noteslist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Anotelist(request,key):
	notelist=Notes.objects.all().filter(pk__exact=key)
	serializer = NotesSerializer(notelist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Atipslist(request):
	tipslist=Tips.objects.all()
	serializer = TipsSerializer(tipslist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aocourseslist(request):
	ocourselist=Onlinecourses.objects.all().filter(visible=True)
	serializer = OnlinecoursesSerializer(ocourselist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Avideolist(request):
	videoslist=Videos.objects.all()
	serializer = VideoSerializer(videoslist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Abookstandardlist(request,key):
	booklist=Books.objects.all().filter(visible=True)
	for i in booklist:
		if(str(i.bgrade) != str(key)):
			booklist=booklist.exclude(pk=i.id)
	serializer = BookSerializer(booklist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquizlist(request,key,reqid):
	qans=Qanswersheet.objects.all().filter(semail=str(reqid))
	quizlist=AddquizT.objects.all().filter(cgrade=int(key))
	for i in qans:
		for j in quizlist:
			if(i.stest == j.cname):
				quizlist=quizlist.exclude(pk=j.id)
	# for i in quizlist:
	# 	if(str(i.bgrade) != str(key)):
	# 		quizlist=quizlist.exclude(pk=i.id)
	serializer = QuizSerializer(quizlist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aattquizlist(request,key):
	attquiz=Qanswersheet.objects.all().filter(semail=str(key))
	serializer = AttquizSerializer(attquiz,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquizanslist(request,key):
	attquizans=AddquestionT.objects.all().filter(testgrade__cname=key)
	serializer = QuizansSerializer(attquizans,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquizansattlist(request,tid,key):
	attquizans=Qanswersheet.objects.all().filter(semail=key,stest=tid)
	serializer = AttquizSerializer(attquizans,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aquizresultlist(request,sid,mil,std,tid,pnt):
	#attquizans=Qanswersheet.objects.all().filter(semail=key,stest=tid)
	#serializer = AttquizSerializer(data=request.data)
	#if serializer.is_valid():
		#serializer.save()
	#Qanswersheet.objects.filter(sname=name,stest=theb).update(sname=name,semail=mail,sgrade=standard,stest=theb,spoint=score)
	Qanswersheet.objects.create(sname=sid,stest=tid,semail=mil,sgrade=std,spoint=pnt)
	attquizans=Qanswersheet.objects.all()
	serializer = AttquizSerializer(attquizans,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Aqresultlist(request,mil):
	Qanswersheet.objects.all().filter(spoint="0",semail=mil).delete()
	Qanswersheet.objects.all().filter(spoint="tempo",semail=mil).delete()
	serializer = QresultSerializer(data=request.data)
	if serializer.is_valid():
		print("SUCCESS")
		serializer.save()
		return Response(serializer.data)
	else:
		print("ERROR")
		print("error",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Amocklist(request,std,mil):
	mocklist=MockPM.objects.all().filter(mpgrade=std)
	mockatt=MockAnswer.objects.all().filter(semail=mil,sgrade=std)
	for i in mockatt:
		for j in mocklist:
			if(i.testname == j.mockpapername):
				mocklist=mocklist.exclude(pk=j.id)
	serializer = MockSerializer(mocklist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aattmocklist(request,tid):
	mockatt=MockAnswer.objects.all().filter(pk=tid)
	serializer = AttMockSerializer(mockatt,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Aattmocknamelist(request,std,mil):
	mockatt=MockAnswer.objects.all().filter(semail=mil,sgrade=std)
	serializer = AttMockSerializer(mockatt,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Amockqplist(request,tid):
	mocklist=MockPM.objects.all().filter(pk=tid)
	serializer = MockSerializer(mocklist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Amtempolist(request,nme,mil):
	attm=MockAnswer.objects.all().filter(testname=nme,semail=mil)
	serializer = AttMockSerializer(attm,many=True)
	return Response(serializer.data)
	# if attm:
	# 	serializer = AttMockSerializer(attm,many=True)
	# 	return Response(serializer.data)
	# else:
	# 	MockAnswer.objects.create(semail=mil,testname=nme,tempo=0)
	# 	serializer = AttMockSerializer(attm,many=True)
	# 	return Response(serializer.data)

@api_view(['POST'])
def Amresultlist(request,mil):
	MockAnswer.objects.all().filter(tempo=0,semail=mil).delete()
	MockAnswer.objects.all().filter(tempo=1,semail=mil).delete()
	MockAnswer.objects.all().filter(tempo=69,semail=mil).delete()
	serializer = AttMockSerializer(data=request.data)
	if serializer.is_valid():
		print("SUCCESS")
		serializer.save()
		return Response(serializer.data)
	else:
		print("ERROR")
		print("error",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Sbooklist(request,grd):
	sbl=Books.objects.all().filter(bgrade__forgrade=grd,visible=True)
	serializer = BookSerializer(sbl,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Squesbank(request,grd):
	quesbank=QPM.objects.all().filter(forgrade=grd)
	serializer = QPbankSerializer(quesbank,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Sbpapers(request,uid):
	quesbank=Paper.objects.all().filter(childpaperfile__parentpaperfile=uid)
	serializer = QpapersSerializer(quesbank,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Srevnotes(request,grd):
	notes=Notes.objects.all().filter(grade=grd)
	serializer = NotesSerializer(notes,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Addbooklist(request):
	serializer = BookSerializer(data=request.data)
	if serializer.is_valid():
		print("SUCCESS")
		serializer.save()
		return Response(serializer.data)
	else:
		print("ERROR")
		print("error",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Atbooklist(request,adb):
	books=Books.objects.all().filter(addedby=adb,visible=True)
	serializer = BookSerializer(books,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Atdelbooklist(request,adb,bid):
	print("here")
	flag=Books.objects.all().filter(addedby=adb,pk__exact=int(bid),visible=True)
	Books.objects.all().filter(addedby=adb,pk__exact=bid).update(visible=False)
	books=Books.objects.all().filter(addedby=adb,visible=True)
	serializer = BookSerializer(books,many=True)
	if(flag):
		stat="success"
		print(stat)
		print(flag)
	else:
		stat="fail"
		print(stat)
		print(flag)
	return Response(serializer.data)

@api_view(['GET'])
def Atexamlist(request,adb):
	exams=MockPM.objects.all().filter(addedby=adb,visible=True)
	serializer = MockSerializer(exams,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Aexamlist(request):
	serializer = MockSerializer(data=request.data)
	if serializer.is_valid():
		print("SUCCESS")
		serializer.save()
		return Response(serializer.data)
	else:
		print("ERROR")
		print("error",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Atdelexamlist(request,adb,bid):
	print("here")
	flag=MockPM.objects.all().filter(addedby=adb,visible=True)
	MockPM.objects.all().filter(addedby=adb,pk__exact=bid).update(visible=False)
	exams=MockPM.objects.all().filter(addedby=adb,visible=True)
	serializer = MockSerializer(exams,many=True)
	if(flag):
		stat="success"
		print(stat)
		print(flag)
	else:
		stat="fail"
		print(stat)
		print(flag)
	return Response(serializer.data)

@api_view(['GET'])
def Atresexamlist(request,adb,bid):
	print("here")
	flag=MockPM.objects.all().filter(addedby=adb,visible=False)
	MockPM.objects.all().filter(addedby=adb,pk__exact=bid).update(visible=True)
	exams=MockPM.objects.all().filter(addedby=adb,visible=True)
	serializer = MockSerializer(exams,many=True)
	if(flag):
		stat="success"
		print(stat)
		print(flag)
	else:
		stat="fail"
		print(stat)
		print(flag)
	return Response(serializer.data)

@api_view(['GET'])
def Aresbooklist(request,adb):
	books=Books.objects.all().filter(addedby=adb,visible=False)
	serializer = BookSerializer(books,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arestorebooklist(request,adb,bid):
	flag=Books.objects.all().filter(addedby=adb,pk__exact=int(bid),visible=False)
	Books.objects.all().filter(addedby=adb,pk__exact=bid).update(visible=True)
	books=Books.objects.all().filter(addedby=adb,visible=True)
	serializer = BookSerializer(books,many=True)
	if(flag):
		stat="success"
	else:
		stat="fail"
	return Response(serializer.data)

@api_view(['GET'])
def Aqpmlist(request):
	qpapers=QPM.objects.all()
	serializer = QPbankSerializer(qpapers,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Apaperlist(request):
	serializer = QpapersSerializer(data=request.data)
	if serializer.is_valid():
		print("SUCCESS")
		serializer.save()
		return Response(serializer.data)
	else:
		print("ERROR")
		print("error",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Aauthorpaperlist(request,mil):
	papers=Paper.objects.all().filter(visible=True,addedby=mil)
	serializer = QpapersSerializer(papers,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Adeletedexam(request,mil):
	delexams=MockPM.objects.all().filter(addedby=mil,visible=False)
	serializer = MockSerializer(delexams,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Adeletepaperlist(request,adb,bid):
	flag=Paper.objects.all().filter(addedby=adb,visible=True,pk__exact=bid).update(visible=False)
	delpaper=Paper.objects.all().filter(addedby=adb,visible=True)
	serializer = QpapersSerializer(delpaper,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arespaper(request,mil):
	respaper=Paper.objects.all().filter(addedby=mil,visible=False)
	serializer = QpapersSerializer(respaper,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arestorepaper(request,mil,bid):
	Paper.objects.all().filter(addedby=mil,visible=False,pk__exact=bid).update(visible=True)
	respaper=Paper.objects.all().filter(addedby=mil,visible=False)
	serializer = QpapersSerializer(respaper,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Aaddquiz(request):
	serializer = QuizSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['POST'])
def Aaddquizquestion(request):
	serializer = QuizansSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def ATquizlist(request,mil):
	quizes=AddquizT.objects.all().filter(author=mil,visible=True)
	serializer = QuizSerializer(quizes,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Adelquizlist(request,mil,bid):
	AddquizT.objects.all().filter(author=mil,visible=True,pk__exact=bid).update(visible=False)
	quizes=AddquizT.objects.all().filter(author=mil,visible=True)
	serializer = QuizSerializer(quizes,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arestorequizlist(request,mil):
	resquiz=AddquizT.objects.all().filter(author=mil,visible=False)
	serializer = QuizSerializer(resquiz,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Arecoverquiz(request,mil,bid):
	AddquizT.objects.all().filter(author=mil,visible=False,pk__exact=bid).update(visible=True)
	resquiz=AddquizT.objects.all().filter(author=mil,visible=True)
	serializer = QuizSerializer(resquiz,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Aaddquizques(request,mil,bid):
	serializer = QuizansSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		quizques=AddquestionT.objects.all().filter(testgrade=bid)
		serializer = QuizansSerializer(quizques,many=True)
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def Aquizques(request,mil,bid):
	flag=AddquizT.objects.all().filter(pk__exact=bid,visible=True)
	if flag:
		resquiz=AddquestionT.objects.all().filter(testgrade=bid)
		serializer = QuizansSerializer(resquiz,many=True)
		return Response(serializer.data)
	else:
		terror="ERROR"
		return Response(terror)

@api_view(['GET'])
def Adelquizques(request,mil,qid,wid):
	flag=AddquizT.objects.all().filter(pk__exact=qid,visible=True,author=mil)
	if flag:
		AddquestionT.objects.all().filter(testgrade=qid,pk__exact=wid).delete()
		resquiz=AddquestionT.objects.all().filter(testgrade=qid)
		serializer = QuizansSerializer(resquiz,many=True)
		return Response(serializer.data)
	else:
		terror="ERROR"
		return Response(terror)

@api_view(['POST'])
def Taddocourse(request,mil):
	serializer = OnlinecoursesSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		ocourses=Onlinecourses.objects.all().filter(visible=True,addedby=mil)
		serializer = OnlinecoursesSerializer(ocourses,many=True)
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def Tocourse(request,mil):
	ocourse=Onlinecourses.objects.all().filter(addedby=mil,visible=True)
	serializer = OnlinecoursesSerializer(ocourse,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tdelocourse(request,mil,cid):
	Onlinecourses.objects.all().filter(addedby=mil,visible=True,pk__exact=cid).update(visible=False)
	ocourse=Onlinecourses.objects.all().filter(addedby=mil,visible=True)
	serializer = OnlinecoursesSerializer(ocourse,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tresocourse(request,mil,cid):
	Onlinecourses.objects.all().filter(addedby=mil,visible=False,pk__exact=cid).update(visible=True)
	delocourse=Onlinecourses.objects.all().filter(addedby=mil,visible=False)
	serializer = OnlinecoursesSerializer(delocourse,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tdellistocourse(request,mil):
	deletedocourse=Onlinecourses.objects.all().filter(addedby=mil,visible=False)
	serializer = OnlinecoursesSerializer(deletedocourse,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tevalpapers(request,mil,std):
	epapers=MockAnswer.objects.all().filter(evaluatedby=mil,evaluated=True,sgrade=std)
	serializer = AttMockSerializer(epapers,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Ttoasspapers(request,std):
	papers=MockAnswer.objects.all().filter(sgrade=std,evaluated=False)
	serializer = AttMockSerializer(papers,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tthatpaper(request,pid):
	paper=MockAnswer.objects.all().filter(pk__exact=pid)
	serializer = AttMockSerializer(paper,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tsubmitpaper(request,pid):
	mpaper=MockAnswer.objects.get(pk__exact=pid)
	serializer = AttMockSerializer(instance=mpaper,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdbookdata(request,pid):
	updbook=Books.objects.all().filter(pk__exact=pid)
	serializer = BookSerializer(updbook,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostbookdata(request,pid):
	book=Books.objects.get(pk__exact=pid)
	serializer = BookSerializer(instance=book,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdexamdata(request,pid):
	updexam=MockPM.objects.all().filter(pk__exact=pid)
	serializer = MockSerializer(updexam,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostexamdata(request,pid):
	exam=MockPM.objects.get(pk__exact=pid)
	serializer = MockSerializer(instance=exam,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		print(serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdqpaperdata(request,pid):
	updqpaper=Paper.objects.all().filter(pk__exact=pid)
	serializer = QpapersSerializer(updqpaper,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostqpaperdata(request,pid):
	qpaper=Paper.objects.get(pk__exact=pid)
	serializer = QpapersSerializer(instance=qpaper,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		print(serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdquizdata(request,pid):
	updquiz=AddquizT.objects.all().filter(pk__exact=pid)
	serializer = QuizSerializer(updquiz,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostquizdata(request,pid):
	quiz=AddquizT.objects.get(pk__exact=pid)
	serializer = QuizSerializer(instance=quiz,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		print(serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdquizquesdata(request,pid):
	updquizques=AddquestionT.objects.all().filter(pk__exact=pid)
	serializer = QuizansSerializer(updquizques,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostquizquesdata(request,pid):
	quizques=AddquestionT.objects.get(pk__exact=pid)
	serializer = QuizansSerializer(instance=quizques,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		print(serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Tupdocoursedata(request,pid):
	updocourse=Onlinecourses.objects.all().filter(pk__exact=pid)
	serializer = OnlinecoursesSerializer(updocourse,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Tpostocoursedata(request,pid):
	ocourse=Onlinecourses.objects.get(pk__exact=pid)
	serializer = OnlinecoursesSerializer(instance=ocourse,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		print(serializer.errors)
		return Response(serializer.errors)

@api_view(['POST'])
def Ssendmessage(request):
	serializer = ChatmessagesSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['POST'])
def Tcreatechatcommunity(request):
	serializer = ChatcommunitiesSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		#chatcomms=AddquestionT.objects.all().filter(testgrade=bid)
		#serializer = QuizansSerializer(quizques,many=True)
		return Response(serializer.data)
	else:
		return Response(serializer.errors)

@api_view(['GET'])
def Aallchatcommunitylist(request):
	commslist=Community.objects.all().filter(visibility=True)
	#commslist=Community.objects.all().filter(comgrade=grd)
	serializer = ChatcommunitiesSerializer(commslist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Agradechatcommunitylist(request,pid):
	commslist=Community.objects.all().filter(visibility=True,pk__exact=pid)
	#commslist=Community.objects.all().filter(comgrade=grd)
	serializer = ChatcommunitiesSerializer(commslist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Sviewmessages(request,pid):
	msgs=Chat.objects.all().filter(communitytype=int(pid),visibility=True)
	print(pid,type(pid))
	serializer = ChatmessagesSerializer(msgs,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Profdetails(request,ml):
	profdetails=CustomUser.objects.all().filter(email=ml)
	serializer = UserSerializer(profdetails,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Updateprofdetails(request,pml):
	user=CustomUser.objects.get(email=pml)
	print(user)
	serializer = UserSerializer(instance=user,data=request.data)
	if serializer.is_valid():
		serializer.save()
		print("Saved")
		return Response(serializer.data)
	else:
		print("not saved",serializer.errors)
		return Response(serializer.errors)

@api_view(['GET'])
def Helplinenumbers(request):
	nunmbers=Helpline.objects.all()
	serializer = HelplineSeriailzer(nunmbers,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Fcompexamlist(request,grd,mil):
	filtcompexam=Addcompexam.objects.all().filter(cgrade=grd,visible=True)
	attcompexam=Compexamresults.objects.all().filter(semail=mil,sgrade=grd)
	for i in filtcompexam:
		for j in attcompexam:
			if(j.stestname==i.cname):
				filtcompexam=filtcompexam.exclude(pk=i.id)
	serializer = CompetitiveexamSerializer(filtcompexam,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Compexamlist(request):
	compexam=Addcompexam.objects.all().filter(visible=True)
	serializer = CompetitiveexamSerializer(compexam,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Compexamques(request,xid):
	'''
	flag=Addcompquestions.objects.all().filter(pk__exact=xid,visible=True)
	if flag:
		resquiz=Addcompquestions.objects.all().filter(testgrade=xid)
		serializer = CexamquestionSerializer(resquiz,many=True)
		return Response(serializer.data)
	else:
		terror="ERROR"
		return Response(terror)
	'''
	compexamques=Addcompquestions.objects.all().filter(testgrade=xid)
	serializer = CexamquestionSerializer(compexamques,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Compexattcheck(request,xid,mid):
	attnd=Compexamresults.objects.all().filter(semail=mid,stest=xid,writting=False)
	serializer = CexamresultSerializer(attnd,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def Compexaddresult(request,sid,xid,mid,std,pnt,crt,wrng,ename):
	#attquizans=Qanswersheet.objects.all().filter(semail=key,stest=tid)
	#serializer = AttquizSerializer(data=request.data)
	#if serializer.is_valid():
		#serializer.save()
	#Qanswersheet.objects.filter(sname=name,stest=theb).update(sname=name,semail=mail,sgrade=standard,stest=theb,spoint=score)
	Compexamresults.objects.all().filter(semail=mid,stest=xid,writting=True).delete()
	Compexamresults.objects.create(sname=sid,stest=xid,semail=mid,sgrade=int(std),spoint=pnt,crt=crt,wrong=wrng,writting=False,stestname=ename)
	attnd=Compexamresults.objects.all()
	serializer = CexamresultSerializer(attnd,many=True)
	return Response(serializer.data)
	'''
	user=Compexamresults.objects.get(email=pml)
	print(user)
	serializer = UserSerializer(instance=user,data=request.data)
	if serializer.is_valid():
		serializer.save()
		print("Saved")
		return Response(serializer.data)
	else:
		print("not saved",serializer.errors)
		return Response(serializer.errors)Aquizresultlist
	'''
@api_view(['POST'])
def Compexaddtemporesult(request,sid,xid,mid,std,ename):
	#attquizans=Qanswersheet.objects.all().filter(semail=key,stest=tid)
	#serializer = AttquizSerializer(data=request.data)
	#if serializer.is_valid():
		#serializer.save()
	#Qanswersheet.objects.filter(sname=name,stest=theb).update(sname=name,semail=mail,sgrade=standard,stest=theb,spoint=score)
	Compexamresults.objects.create(sname=sid,stest=xid,semail=mid,sgrade=int(std),stestname=ename)
	attnd=Compexamresults.objects.all()
	serializer = CexamresultSerializer(attnd,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Compexquestions(request,xid):
	questions=Addcompquestions.objects.all().filter(testgrade=xid)
	serializer = CexamquestionSerializer(questions,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tutorslist(request,grd):
	tutorlist=CustomUser.objects.all().filter(advertise=True,teacher=True,standard=grd)
	serializer = UserSerializer(tutorlist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Atutorslist(request):
	alltutorlist=CustomUser.objects.all().filter(teacher=True)
	serializer = UserSerializer(alltutorlist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Tallcompexlist(request):
	allcompexlist=Addcompexam.objects.all().filter(visible=True)
	serializer = CompetitiveexamSerializer(allcompexlist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Compexkeys(request,xid):
	allcompexanslist=Addcompquestions.objects.all().filter(testgrade=xid)
	serializer = CexamquestionSerializer(allcompexanslist,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Sattcompex(request,mid):
	allattcompexanslist=Compexamresults.objects.all().filter(semail=mid)
	serializer = CexamresultSerializer(allattcompexanslist,many=True)
	return Response(serializer.data)