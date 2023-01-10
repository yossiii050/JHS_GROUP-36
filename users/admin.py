from django.contrib import admin
from .models import Employer, Candidate,CVFormModel,staffUser


admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(CVFormModel)
admin.site.register(staffUser)
