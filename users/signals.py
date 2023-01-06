from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employer, Candidate, EmployerProfile, CandidateProfile
from django.contrib.auth.models import User

@receiver(post_save, sender=(Employer,Candidate))
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_employer:
            Employer.objects.create(user=instance)
            EmployerProfile.objects.create(employer=instance.employer)
        elif instance.is_candidate:
            Candidate.objects.create(user=instance)
            CandidateProfile.objects.create(candidate=instance.candidate)

