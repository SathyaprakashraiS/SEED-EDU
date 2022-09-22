from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import News
from .forms import CustomUserForm
from .models import Dialogues

class CustomUserAdmin(UserAdmin):
	UserAdmin.list_display += ('teacher','status','remark','standard','img','hide','advertise','needassist','resume','contactnumber')
	UserAdmin.list_filter += ('teacher','status','remark','standard','img','hide','advertise','needassist','resume','contactnumber')
	UserAdmin.fieldsets += (('teacher', {'fields': ('teacher','status','remark','standard','img','hide','advertise','needassist','resume','contactnumber')}),) 
  
 
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(News)
admin.site.register(Dialogues)