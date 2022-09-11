from django.urls import path,include
from . import views
from main.views import GoogleLogin

urlpatterns=[
path("",views.home,name="home"),
path("game/",views.game,name="game"),
path("home/",views.home,name="home"),
path("news/",views.news,name="news"),
path("edit/",views.edit,name="profedit"),
path("view/",views.view,name="profview"),
path("news-list/",views.Anewslist,name="news-api"),
path("users-list/",views.Auserslist,name="users-api"),
path("books-list/",views.Abooklist,name="books-api"),
path("acollege-list/",views.Aallcollegelist,name="colleges-api"),
path("tcollege-list/",views.Atopcollegelist,name="colleges-api"),
path("dcollege-list/",views.Adegreecollegelist,name="colleges-api"),
path("scollege-list/",views.Astatecollegelist,name="colleges-api"),
path("ccollege-list/",views.Acitycollegelist,name="colleges-api"),
path("coursecollege-list/",views.Acoursecollegelist,name="colleges-api"),
path("paper-list/",views.Apaperlist,name="papers-api"),
path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
path("artscourse-list/",views.Aartscourselist,name="arts-api"),
path("sciencecourse-list/",views.Asciencecourselist,name="science-api"),
path("engineeringcourse-list/",views.Aengineeringcourselist,name="engineering-api"),
path("commercecourse-list/",views.Acommercecourselist,name="commerce-api"),
path("professionalcourse-list/",views.Aprofessionalcourselist,name="professional-api"),
path("dates-list/",views.Adateslist,name="dates-api"),
path("qptypes-list/",views.Aquestionbanktypeslist,name="qpbanktypes-api"),
path("qps-list/<str:key>/",views.Aquestionbanklist,name="qpbank-api"),
path("rnotes-list/",views.Arnoteslist,name="rnotes-api"),
path("rnotes-list/<str:key>/",views.Anotelist,name="note-api"),
path("tips-list/",views.Atipslist,name="tips-api"),
path("ocourses-list/",views.Aocourseslist,name="ocourses-api"),
path("videos-list/",views.Avideolist,name="videos-api"),
path("sbooks-list/<str:key>/",views.Abookstandardlist,name="standardbook-api"),
path("quiz-list/<str:key>/<str:reqid>/",views.Aquizlist,name="quiz-api"),
path("attquiz-list/<str:key>/",views.Aattquizlist,name="attquiz-api"),
path("quizans-list/<str:key>/",views.Aquizanslist,name="quizans-api"),
path("quizansatt-list/<str:tid>/<str:key>/",views.Aquizansattlist,name="quizans-api"),
path("quizresult-list/<str:sid>/<str:mil>/<str:std>/<str:tid>/<str:pnt>/",views.Aquizresultlist,name="quizresult-api"),
path("quizrresult-list/<str:mil>/",views.Aqresultlist,name="quizresult-api"),
path("mock-list/<str:std>/<str:mil>/",views.Amocklist,name="mock-api"),
path("attmock-list/<str:std>/<str:mil>/",views.Aattmocknamelist,name="attmock-api"),
path("viewmockans-list/<str:tid>/",views.Aattmocklist,name="attmock-api"),
path("mockqp-list/<str:tid>/",views.Amockqplist,name="mockqp-api"),
path("mocktempo-list/<str:nme>/<str:mil>/",views.Amtempolist,name="temporesult-api"),
path("mockrresult-list/<str:mil>/",views.Amresultlist,name="mockresult-api"),
path("sbook-list/<str:grd>/",views.Sbooklist,name="sbook-api"),
path("qptypes-list/<str:grd>/",views.Squesbank,name="squesbank-api"),
path("bpapers-list/<str:uid>/",views.Sbpapers,name="sbpapers-api"),
path("revnotes-list/<str:grd>/",views.Srevnotes,name="srevnotes-api"),
path("addbook-list/",views.Addbooklist,name="addbooks-api"),
path("tbook-list/<str:adb>/",views.Atbooklist,name="teacherviewbooks-api"),
path("tdelbook-list/<str:adb>/<str:bid>/",views.Atdelbooklist,name="delTbooks-api"),
path("texam-list/<str:adb>/",views.Atexamlist,name="dispexam-api"),
path("addexam-list/",views.Aexamlist,name="addexam-api"),
path("tdelexam-list/<str:adb>/<str:bid>/",views.Atdelexamlist,name="delexams-api"),
path("tresexam-list/<str:adb>/<str:bid>/",views.Atresexamlist,name="resexams-api"),
path("tresbook-list/<str:adb>/",views.Aresbooklist,name="delbook-list-api"),
path("trestorebook-list/<str:adb>/<str:bid>/",views.Arestorebooklist,name="resbook-api"),
path("tqptypes-list/",views.Aqpmlist,name="quespapertypes-api"),
path("addpaper-list/",views.Apaperlist,name="addqpaper-api"),
path("delpaper-list/<str:adb>/<str:bid>/",views.Adeletepaperlist,name="delqpaper-api"),
path("Authpaper-list/<str:mil>/",views.Aauthorpaperlist,name="delpaperlist-api"),
path("Tdeletedexam-list/<str:mil>/",views.Adeletedexam,name="deletedpaperlist-api"),
path("respaper-list/<str:mil>/",views.Arespaper,name="restorepaperlist-api"),
path("recoverpaper-list/<str:mil>/<str:bid>/",views.Arestorepaper,name="recoverpaperlist-api"),
path("Taddquiz-list/",views.Aaddquiz,name="addquiz-api"),
path("Taddquizquestion-list/",views.Aaddquizquestion,name="addquizquestion-api"),
path("Tquiz-list/<str:mil>/",views.ATquizlist,name="quizlist-api"),
path("Tdelquiz-list/<str:mil>/<str:bid>/",views.Adelquizlist,name="delquizlist-api"),
path("Trestorequiz-list/<str:mil>/",views.Arestorequizlist,name="restorequizlist-api"),
path("Trestorequiz-list/<str:mil>/<str:bid>/",views.Arecoverquiz,name="restorequizlist-api"),
path("Taddquizques-list/<str:mil>/<str:bid>/",views.Aaddquizques,name="addquizqueslist-api"),
path("Tquizques-list/<str:mil>/<str:bid>/",views.Aquizques,name="quizquestionlist-api"),
path("Tdelquizques-list/<str:mil>/<str:qid>/<str:wid>/",views.Adelquizques,name="quizquestionlist-api"),
path("Taddocourse-list/<str:mil>/",views.Taddocourse,name="addcourselist-api"),
path("Tocourse-list/<str:mil>/",views.Tocourse,name="ocourseslist-api"),
path("Tdelocourse-list/<str:mil>/<str:cid>/",views.Tdelocourse,name="deleteaocourseslist-api"),
path("Tresocourse-list/<str:mil>/<str:cid>/",views.Tresocourse,name="restoreocourseslist-api"),
path("Tdeletedocourses-list/<str:mil>/",views.Tdellistocourse,name="deletedocourseslist-api"),
path("TEvalpapers-list/<str:mil>/<str:std>/",views.Tevalpapers,name="evaluatedpaperlist-api"),
path("Ttoasspapers-list/<str:std>/",views.Ttoasspapers,name="notevaluatedpaperlist-api"),
path("Tthatpaper/<str:pid>/",views.Tthatpaper,name="studexampaper-api"),
path("Tcorrectedsubmitpaper/<str:pid>/",views.Tsubmitpaper,name="poststudexampaper-api"),
path("Tupdatebookdata/<str:pid>/",views.Tupdbookdata,name="bookupdatedata-api"),
path("Tpostupdatedbookdata/<str:pid>/",views.Tpostbookdata,name="postupdatedbookdata-api"),
path("Tupdateexamdata/<str:pid>/",views.Tupdexamdata,name="examupdatedata-api"),
path("Tpostupdatedexamdata/<str:pid>/",views.Tpostexamdata,name="postupdatedexamdata-api"),
path("Tupdateqpaperdata/<str:pid>/",views.Tupdqpaperdata,name="qpaperupdatedata-api"),
path("Tpostupdatedqpaperdata/<str:pid>/",views.Tpostqpaperdata,name="postupdatedqpaperdata-api"),
path("Tupdatequizdata/<str:pid>/",views.Tupdquizdata,name="quizupdatedata-api"),
path("Tpostupdatedquizdata/<str:pid>/",views.Tpostquizdata,name="postupdatedquizdata-api"),
path("Tupdatequizquesdata/<str:pid>/",views.Tupdquizquesdata,name="quizquesupdatedata-api"),
path("Tpostupdatedquizquesdata/<str:pid>/",views.Tpostquizquesdata,name="postupdatedquizquesdata-api"),
path("Tupdateocoursedata/<str:pid>/",views.Tupdocoursedata,name="ocourseupdatedata-api"),
path("Tpostupdatedocoursedata/<str:pid>/",views.Tpostocoursedata,name="postupdatedocoursedata-api"),
path("Tviewchatcomm/",views.Aallchatcommunitylist,name="chatgrouplist-api"),
path("Tcreatechatcomm/",views.Tcreatechatcommunity,name="createanewchatgroup-api"),
path("Tsendchatcomm/",views.Ssendmessage,name="sendchattogroup-api"),
path("Aviewchatcomm/<str:pid>/",views.Sviewmessages,name="viewchatmsgs-api")
]