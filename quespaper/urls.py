from django.urls import path,include
from . import views

urlpatterns=[
path("",views.qpmain,name="qpmain"),
path("showqp/",views.showqp,name="showqp"),
]