from django.contrib import admin
from .models import Candidate
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib.auth.models import User 
admin.site.register(Candidate)

#admin.site.register(CreateCandidateForm)