from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model): #The dataBase knows to create a table for this model
    title=models.CharField(max_length=50,null=True)
    subTitle=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True) #automaticly applied

    def __str__(self):
        return self.title



# Create your models here.
