from django.contrib import admin
from .models import Commerce
from .models import Science
from .models import Architecture
from .models import Defence
from .models import Biology
from .models import Government
from .models import Fashiondesign
from .models import Mathematics
from .models import Socialscience
from .models import Postgraduation

# Register your models here.
admin.site.register(Commerce)
admin.site.register(Science)
admin.site.register(Architecture)
admin.site.register(Defence)
admin.site.register(Biology)
admin.site.register(Government)
admin.site.register(Fashiondesign)
admin.site.register(Mathematics)
admin.site.register(Socialscience)
admin.site.register(Postgraduation)