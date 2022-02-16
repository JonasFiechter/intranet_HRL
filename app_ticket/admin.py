from django.contrib import admin
from app_ticket.models import Ticket, Sector

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'date', 'status', 'description']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector)