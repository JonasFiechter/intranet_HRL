from django.contrib import admin

from app_ticket.models import Category, Status, Ticket

# Register your models here.

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Ticket)