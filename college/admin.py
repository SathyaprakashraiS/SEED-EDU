from django.contrib import admin
from .models import Allcollege
from .models import Topcollege
from .models import Statecollege
from .models import Citycollege
from .models import Degreecollege
from .models import Coursebasedcollege

from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export import resources

class CollegeResource(resources.ModelResource):
    myfield = Field(column_name='myfield')

    class Meta:
        model = Allcollege

class CollegeAdmin(ImportExportModelAdmin):
    resource_class = CollegeResource

admin.site.register(Allcollege, CollegeAdmin)

# # Register your models here.
# admin.site.register(Allcollege)
admin.site.register(Topcollege)
admin.site.register(Statecollege)
admin.site.register(Citycollege)
admin.site.register(Degreecollege)
admin.site.register(Coursebasedcollege)