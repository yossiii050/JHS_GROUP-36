from django import template
from users.views import ReportUsers

register = template.Library()

@register.simple_tag
def report_users():
    return ReportUsers()