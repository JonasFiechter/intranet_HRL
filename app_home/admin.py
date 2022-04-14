from django.contrib import admin
from app_home.models import PhoneExtensions, FunctionsBySector

class PhoneExtensionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch', 'sector', 'floor', 'description']


class FunctionsBySectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'branch', 'sector', 'description']

admin.site.register(PhoneExtensions, PhoneExtensionsAdmin)
admin.site.register(FunctionsBySector, FunctionsBySectorAdmin)