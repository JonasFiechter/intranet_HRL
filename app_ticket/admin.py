from django.contrib import admin
from app_ticket.models import Ticket, Sector, MachineType


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'sector', 'date', 'description', 'category', 'response_user', 'status']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sector_name']


class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'machine_name']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(MachineType, MachineTypeAdmin)