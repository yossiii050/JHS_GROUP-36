from django.contrib import admin
from .models import Ticket

class ticketAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']

admin.site.register(Ticket, ticketAdmin)
