from django.urls import path,include
from . import views

from .views import *

urlpatterns=[
path("",views.home,name="home"),
path("ECRUD/update/<pk>",updateMock.as_view(),name="update-mock"),
path("asses/",views.asses,name="asses"),
path("addcourse/",views.addcourse,name="addcourse"),
path("addquestion/",views.addquestion,name="addquestion"),
path("testpaper/",views.assespaper,name="assespaper"),
path("testpaper/savepaper/",views.saveassespaper,name="saveassespaper"),
path("checkpaper/",views.checkpaper,name="checkpaper"),
path("QCRUD/",views.addquiz,name="addquiz"),
path("addquizques/",views.addquizques,name="addquizques"),
path("caddquiz/",views.createaddquiz,name="createaddquiz"),
path("QCRUD/delquiz/",views.delquiz,name="delquiz"),
path("QCRUD/delques/",views.delques,name="delques"),
path("QCRUD/delques/delquizques/",views.delquizques,name="delquizques"),

path("ECRUD/",views.ECRUD,name="ECRUD"),
path("ECRUD/addexam/",views.addexam,name="addexam"),
path("ECRUD/delexam/",views.delexam,name="delexam"),
# path("ECRUD/modexam/",views.modexam,name="modexam"),
]