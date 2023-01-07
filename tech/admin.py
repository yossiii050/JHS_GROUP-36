from django.contrib import admin
from .models import Ticket

class ticketAdmin(admin.ModelAdmin):
    list_display = ['title', 'body','date','user','closed_by','isopen']

admin.site.register(Ticket, ticketAdmin)
