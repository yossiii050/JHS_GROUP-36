from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(("Main claim"), max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='user',blank=True,null=True)
    handler = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='handler',blank=True,null=True)
    isopen = models.BooleanField(default=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='closed_by',blank=True,null=True)
    #closed_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='closed_by',blank=True,null=True)

    Reply=models.TextField(blank=True,default=" ")
    def __str__(self):
        return self.title


#def numofUser()
 #   users = User.objects.all()
  #  return Response(len(users))

