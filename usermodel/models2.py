from django.db import models
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.models import AbstractUser

class EmployerUser(AbstractUser):
    class Meta:
        verbose_name = "Employers-User"

    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_perms')
    def __str__(self):
           return self.username