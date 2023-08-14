from django.contrib import admin
from .models import User,Service
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("service_type", "service_name",)

admin.site.register(Service,MemberAdmin)



class UserAdmin(admin.ModelAdmin):
  list_display = ("firstname","service_type", "status",)

admin.site.register(User,UserAdmin)