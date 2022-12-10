from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    user2=models.CharField(max_length=200,null=True)

    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
