from django.contrib import admin
from .models import Art
from .models import Science
from .models import Engineering
from .models import Commerce
from .models import Professional
from .models import TCourse

# Register your models here.
admin.site.register(TCourse)
admin.site.register(Art)
admin.site.register(Science)
admin.site.register(Engineering)
admin.site.register(Commerce)
admin.site.register(Professional)