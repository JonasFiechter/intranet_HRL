from django.contrib import admin
from app_home.models import PhoneExtensions

class PhoneExtensionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch', 'sector', 'floor', 'description']


admin.site.register(PhoneExtensions, PhoneExtensionsAdmin)