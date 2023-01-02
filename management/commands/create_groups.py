from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create the "candidate" group and assign the "view_candidate_page" permission
        candidate_group = Group.objects.create(name='candidates')
        view_candidate_page_permission = Permission.objects.get(codename='view_candidate_page')
        candidate_group.permissions.add(view_candidate_page_permission)

        # Create the "employer" group and assign the "view_employer_page" permission
        employer_group = Group.objects.create(name='employers')
        view_employer_page_permission = Permission.objects.get(codename='view_employer_page')
        employer_group.permissions.add(view_employer_page_permission)

        # Create the "manager" group and assign the "view_manager_page" permission
        manager_group = Group.objects.create(name='managers')
        view_manager_page_permission = Permission.objects.get(codename='view_manager_page')
        manager_group.permissions.add(view_manager_page_permission)
