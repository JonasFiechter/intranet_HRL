from django.contrib import admin
from .models import Messages

# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file']

admin.site.register(Messages, MessagesAdmin)