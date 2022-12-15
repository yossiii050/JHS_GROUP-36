from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Upload(models.Model): #The dataBase knows to create a table for this model
    title=models.CharField(max_length=50,null=True)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)
    subTitle=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True) #automaticly applied

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...' #take from 0 to 50 characters

    def get_absolute_url(self):
        return reverse("upload_detail", kwargs={"slug": self.slug})


# Create your models here.