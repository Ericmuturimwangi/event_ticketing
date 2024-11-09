from django.contrib import admin
from .models import Event, Ticket, Order


class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'type', 'price', 'available_quantity')
    search_fields = ['event__title', 'type']


class OrderAdmin(admin.ModelAdmin):
    list_display =('user', 'event', 'ticket', 'quantity', 'total_price', 'status')
    list_filter = ['status', 'event']
    search_fields =['user__username', 'event__title']

admin.site.register(Event)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Order, OrderAdmin)

