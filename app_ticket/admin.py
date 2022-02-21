from django.contrib import admin
from app_ticket.models import Ticket, Sector


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'sector', 'date', 'description', 'category', 'status']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sector_name']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector, SectorAdmin)