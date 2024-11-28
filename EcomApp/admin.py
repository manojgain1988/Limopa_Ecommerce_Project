from django.contrib import admin
from EcomApp .models import Setting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['id','title','email','contact','status','created_at','updated_at']

admin.site.register(Setting, SettingAdmin)