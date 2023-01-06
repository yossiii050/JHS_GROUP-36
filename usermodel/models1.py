from django.db import models
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.models import AbstractUser

class CandidateUser(AbstractUser):
    class Meta:
        verbose_name = "Candidates-Users"
    user_id = models.CharField(max_length=30,default='')
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='myuser2_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='myuser2_perms')

    def __str__(self):
        return self.username