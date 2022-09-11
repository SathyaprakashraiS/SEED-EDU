from django.urls import path,include
from . import views
from main.views import GoogleLogin

urlpatterns=[
path("",views.chome,name="commshome"),
path("cten/",views.cten,name="commsten")
]