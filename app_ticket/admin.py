from django.contrib import admin
from app_ticket.models import Category, Ticket, Sector


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'date', 'status', 'description', 'category']


class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'sector_name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'sector']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Category, CategoryAdmin)