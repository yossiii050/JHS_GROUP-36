from django import template
from users.views import ReportUsers
from django.contrib.auth.models import Group,User
register = template.Library()

@register.simple_tag
def report_users1():
    return ReportUsers(User)