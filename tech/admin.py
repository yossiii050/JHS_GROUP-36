from django.contrib import admin
from .models import ticket

class ticketAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']

admin.site.register(ticket, ticketAdmin)
