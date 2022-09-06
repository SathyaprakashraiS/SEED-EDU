from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("FAQ/",views.FAQ,name="FAQ"),
path("rnotes/",views.rnotes,name="rnotes"),
path("tips/",views.tips,name="tips"),
path("rnotes/read/",views.readrnotes,name="read notes"),
path("courses/",views.courses,name="ocourse"),
path("vids/",views.vids,name="videos")
]