from django.contrib import admin
from .models import Candidate , CVForm
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib.auth.models import User 
admin.site.register(Candidate)
admin.site.register(CVForm)
#admin.site.register(CreateCandidateForm)

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

