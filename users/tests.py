from django.test import TestCase
from .forms import CreateEmployerForm,CreateCandidateForm
from django.contrib.auth import get_user_model,authenticate
import datetime
from datetime import date,timedelta
from collections import OrderedDict
from asyncio import Task
from users.models import Candidate,User
from django.urls import reverse


class ReportViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_Candidate = 7
        number_of_User = 7

        for user_id in range(number_of_User):
                User.objects.create(
                    first_name=f'Dominique {user_id}',
                    last_name=f'Surname {user_id}',
                )
        for user_id in range(number_of_Candidate):
                Candidate.objects.create(
                    first_name=f'Dominique {user_id}',
                    last_name=f'Surname {user_id}',
                )        
    



class SigninTestEmployer(TestCase):

    def setUp(self):
        self.CreateEmployerForm = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.CreateEmployerForm.save()

    def tearDown(self):
        self.CreateEmployerForm.delete()

    def test_correct(self):
        CreateEmployerForm = authenticate(username='test', password='12test12')
        self.assertTrue((CreateEmployerForm is not None) and CreateEmployerForm.is_authenticated)

    def test_wrong_username(self):
        CreateEmployerForm = authenticate(username='wrong', password='12test12')
        self.assertFalse(CreateEmployerForm is not None and CreateEmployerForm.is_authenticated)

    def test_wrong_pssword(self):
        CreateEmployerForm = authenticate(username='test', password='wrong')
        self.assertFalse(CreateEmployerForm is not None and CreateEmployerForm.is_authenticated)

class SigninTestCandidate(TestCase):

    def setUp(self):
        self.CreateCandidateForm = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.CreateCandidateForm.save()

    def tearDown(self):
        self.CreateCandidateForm.delete()

    def test_correct(self):
        CreateCandidateForm = authenticate(username='test', password='12test12')
        self.assertTrue((CreateCandidateForm is not None) and CreateCandidateForm.is_authenticated)

    def test_wrong_username(self):
        CreateCandidateForm = authenticate(username='wrong', password='12test12')
        self.assertFalse(CreateCandidateForm is not None and CreateCandidateForm.is_authenticated)

    def test_wrong_pssword(self):
        CreateCandidateForm = authenticate(username='test', password='wrong')
        self.assertFalse(CreateCandidateForm is not None and CreateCandidateForm.is_authenticated)        


