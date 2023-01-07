from django.contrib import admin
from .models import Employer, Candidate, EmployerProfile, CandidateProfile,CVFormModel

class EmployerProfileInline(admin.StackedInline):
    model = EmployerProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CandidateProfileInline(admin.StackedInline):
    model = CandidateProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class EmployerAdmin(admin.ModelAdmin):
    inlines = (EmployerProfileInline,)

class CandidateAdmin(admin.ModelAdmin):
    inlines = (CandidateProfileInline,)

admin.site.register(Employer, EmployerAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CVFormModel)
