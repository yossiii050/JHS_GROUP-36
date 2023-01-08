from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import Employer, Candidate
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create 20 Employer instances
        for i in range(10):
            employer = Employer(
                email=f'employer{i}@example.com',
                username=f'employer{i}',
                CompanyName=f'Company {i}',
                employer_id=f'employer{i}',
                is_employer=True,
                bios='Write your bio here...',
            )
            employer.set_password('password')
            employer.save()
        
        # Create 20 Candidate instances
        candidates = []
        for i in range(10):
            candidate = Candidate(
                email=f'candidate{i}@example.com',
                username=f'candidate{i}',
                candidate_id=f'candidate{i}',
                date_of_birth='2000-01-01',
                phone_number='1234567890',
                first_name='First',
                last_name='Last',
                is_candidate=True,
                bios='Write your bio here...',
            )
            candidate.set_password('password')
            candidates.append(candidate)
        Candidate.objects.bulk_create(candidates)