from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("",views.college,name="colleges"),
path("allcolleges/",views.allcollege,name="Allcolleges"),
path("topcolleges/",views.topcollege,name="Topcolleges"),
path("degreebasedcolleges/",views.degreebasedcollege,name="Degreebasedcolleges"),
path("statebasedcolleges/",views.statebasedcollege,name="Statebasedcolleges"),
path("citybasedcolleges/",views.citybasedcollege,name="Citybasedcolleges"),
path("coursebasedcolleges/",views.coursebasedcollege,name="Coursebasedcolleges")
]