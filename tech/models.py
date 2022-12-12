from django.db import models
from django.contrib.auth.models import User

class ticket(models.Model):
    title = models.CharField(("Sumbit your ticket"), max_length=50)
    body = models.TextField()
    #date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
           return self.title

