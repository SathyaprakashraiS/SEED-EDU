from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("",views.books,name="library"),
path("book/",views.viewbook,name="BookClass"),
path("twelve/",views.twelth,name="twelth"),
path("eleven/",views.eleventh,name="eleventh"),
path("ten/",views.tenth,name="tenth"),
path("neet/",views.neet,name="neet"),
path("jeemain/",views.jeemain,name="jeemain"),
path("jeeadvance/",views.jeeadvance,name="jeeadvance")
]