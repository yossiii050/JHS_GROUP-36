from django.db import models
from django.contrib.auth.models import User

class ticket(models.Model):
    title = models.CharField(("Main claim"), max_length=50)
    body = models.TextField()
    #date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
           return self.title

#def numofUser()
 #   users = User.objects.all()
  #  return Response(len(users))

