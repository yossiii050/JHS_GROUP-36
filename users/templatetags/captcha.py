from django import template
#from users.views import ReportUsers
from captcha.fields import CaptchaField

captcha = template.Library()

@captcha.simple_tag
def captcha():
    return CaptchaField()