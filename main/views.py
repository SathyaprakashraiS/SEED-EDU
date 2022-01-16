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
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
#from django.contrib.auth.models import User



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
	ocourselist=Onlinecourses.objects.all()
	serializer = OnlinecoursesSerializer(ocourselist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Avideolist(request):
	videoslist=Videos.objects.all()
	serializer = VideoSerializer(videoslist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def Abookstandardlist(request,key):
	booklist=Books.objects.all()
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
	if attm:
		serializer = AttMockSerializer(attm,many=True)
		return Response(serializer.data)
	else:
		MockAnswer.objects.create(semail=mil,testname=nme,tempo=69)
		serializer = AttMockSerializer(attm,many=True)
		return Response(serializer.data)

@api_view(['POST'])
def Amresultlist(request,mil):
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
	sbl=Books.objects.all().filter(bgrade__forgrade=grd)
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