from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
    title = models.CharField(("Main claim"), max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user')
    handler = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='handler')
    def __str__(self):
        return self.title


#def numofUser()
 #   users = User.objects.all()
  #  return Response(len(users))

