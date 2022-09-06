from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("",views.test,name="test"),
path("commerce/",views.commerce,name="commerce"),
path("biology/",views.biology,name="biology"),
path("archietecture/",views.archietecture,name="archietecture"),
path("government/",views.government,name="government"),
path("fashiondesign/",views.fashiondesign,name="fashiondesign"),
path("science/",views.science,name="science"),
path("defence/",views.defence,name="defence"),
path("mathematics/",views.mathematics,name="mathematics"),
path("socialscience/",views.socialscience,name="socialscience"),
path("postgrad/",views.postgrad,name="postgraduation")
]