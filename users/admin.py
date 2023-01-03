from django.contrib import admin
from .models import Candidate ,EmployerProfile,CVFormModel
from .forms import CreateEmployerForm
from django.contrib.auth.models import User 
admin.site.register(Candidate)
admin.site.register(CVFormModel)
#admin.site.register(CreateCandidateForm)

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

admin.site.register(EmployerProfile)