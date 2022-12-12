from django.db import models

class Ticket(models.Model):
    title = models.models.CharField(("Sumbit your ticket"), max_length=50)
    body = models.TextField()
    
    
