from django.contrib import admin
from app_ticket.models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'sector', 'date', 'description', 'category', 'response_user', 'status']
    link_display = ['requester_name']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sector_name']


class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'machine_name']


class TransportRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'date', 'requester_name', 'sector', 'destination_address', 'response_user']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(MachineType, MachineTypeAdmin)
admin.site.register(TransportRequest, TransportRequestAdmin)