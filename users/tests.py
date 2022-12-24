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


class CandidateTestCase(TestCase):
    def setUp(self):
        # create a candidate object to use in the tests
        self.candidate = Candidate.objects.create(
            username='testuser',
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='testpass',
            Id='123456789',
            date_of_birth='2000-01-01',
            phone_number='+1234567890'
        )

    def test_candidate_username(self):
        # test that the candidate's username is set correctly
        self.assertEqual(self.candidate.username, 'testuser')

    def test_candidate_email(self):
        # test that the candidate's email is set correctly
        self.assertEqual(self.candidate.email, 'testuser@example.com')

    def test_candidate_first_name(self):
        # test that the candidate's first name is set correctly
        self.assertEqual(self.candidate.first_name, 'Test')

    def test_candidate_last_name(self):
        # test that the candidate's last name is set correctly
        self.assertEqual(self.candidate.last_name, 'User')

    def test_candidate_password(self):
        # test that the candidate's password is set correctly
        self.assertEqual(self.candidate.password, 'testpass')

    def test_candidate_id(self):
        # test that the candidate's ID is set correctly
        self.assertEqual(self.candidate.Id, '123456789')

    def test_candidate_date_of_birth(self):
        # test that the candidate's date of birth is set correctly
        self.assertEqual(self.candidate.date_of_birth, '2000-01-01')

    def test_candidate_phone_number(self):
        # test that the candidate's phone number is set correctly
        self.assertEqual(self.candidate.phone_number, '+1234567890')