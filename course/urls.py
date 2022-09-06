from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("",views.courses,name="courses"),
path("arts/",views.arts,name="arts"),
path("science/",views.science,name="science"),
path("engineering/",views.engineering,name="engineering"),
path("commerce/",views.commerce,name="commerce"),
path("procourse/",views.procourse,name="procourse")
]