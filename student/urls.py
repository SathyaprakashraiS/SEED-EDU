from django.urls import path,include
from . import views

urlpatterns=[
path("",views.home,name="home"),
path("quizwarner/",views.quizwarner,name="quizwarner"),
path("quizwarner/quiz/",views.quiz,name="quiz"),
path("quizwarner/quiz/quizresult/",views.quizresult,name="quizresult"),
path("quiz/",views.quiz,name="quiz"),
path("quiz/quizresult/",views.quizresult,name="quizresult"),
path("quizans/",views.quizans,name="quizanswer"),
path("mockexam/",views.mockexam,name="mock"),
path("mockwarner/",views.mockwarner,name="mock"),
path("mockwarner/mockexam/",views.mockexam,name="mock"),
path("book/",views.book,name="book"),
]