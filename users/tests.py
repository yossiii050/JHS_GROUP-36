from django.test import TestCase
from django.contrib.auth import get_user_model,authenticate
from .models import Employer, Candidate
from .forms import EmployerSignUpForm, CandidateSignUpForm, CandidateForm, EmployerForm
from users.models import Candidate,User
from django.urls import reverse
from users.views import ReportUsers
from django.http import HttpRequest
from django.contrib.auth.models import Group,User

class ReportVIPUsersViewTests(TestCase):
    def test_view_only_accessible_to_staff(self):
        response = self.client.get(reverse('VipUsers'))
        self.assertEqual(response.status_code, 302)

        staff_user = User.objects.create_user(
            username='staff', password='password', is_staff=True)
        self.client.login(username='staff', password='password')

        response = self.client.get(reverse('home page'))
        self.assertEqual(response.status_code, 200)

    def test_vip_users_are_shown_in_template(self):
        staff_user = User.objects.create_user(
            username='staff', password='password', is_staff=True)
        self.client.login(username='staff', password='password')

        vip_group = Group.objects.create(name='VIP')
        vip_user1 = User.objects.create_user(
            username='vip1', password='password')
        vip_user1.groups.add(vip_group)
        vip_user2 = User.objects.create_user(
            username='vip2', password='password')
        vip_user2.groups.add(vip_group)

        response = self.client.get(reverse('VipUsers'))
        self.assertContains(response, 'vip1')
        self.assertContains(response, 'vip2')


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
    
class EmployerModelTests(TestCase):
    def test_employer_creation(self):
        # Create a new employer
        user = User.objects.create_user(
            username='employer1', email='employer1@example.com', password='testpass'
        )
        employer = Employer.objects.create(
            user=user,
            email='employer1@example.com',
            username='employer1',
            CompanyName='Test Company',
            employer_id='12345',
            is_employer=True,
            bios='Test employer bio'
        )

        # Check that the employer was created correctly
        self.assertEqual(employer.user.username, 'employer1')
        self.assertEqual(employer.email, 'employer1@example.com')
        self.assertEqual(employer.username, 'employer1')
        self.assertEqual(employer.CompanyName, 'Test Company')
        self.assertEqual(employer.employer_id, '12345')
        self.assertTrue(employer.is_employer)
        self.assertEqual(employer.bios, 'Test employer bio')

class CandidateModelTests(TestCase):
    def test_candidate_creation(self):
        # Create a new candidate
        user = User.objects.create_user(
            username='candidate1', email='candidate1@example.com', password='testpass'
        )
        candidate = Candidate.objects.create(
            user=user,
            email='candidate1@example.com',
            username='candidate1',
            candidate_id='12345',
            date_of_birth='2000-01-01',
            phone_number='123-456-7890',
            first_name='Test',
            last_name='Candidate',
            is_candidate=True,
            bios='Test candidate bio'
        )

        # Check that the candidate was created correctly
        self.assertEqual(candidate.user.username, 'candidate1')
        self.assertEqual(candidate.email, 'candidate1@example.com')
        self.assertEqual(candidate.username, 'candidate1')
        self.assertEqual(candidate.candidate_id, '12345')
        self.assertEqual(candidate.date_of_birth, '2000-01-01')
        self.assertEqual(candidate.phone_number, '123-456-7890')
        self.assertEqual(candidate.first_name, 'Test')
        self.assertEqual(candidate.last_name, 'Candidate')
        self.assertTrue(candidate.is_candidate)
        self.assertEqual(candidate.bios, 'Test candidate bio')

class EmployerSignUpFormTests(TestCase):
    def test_form_validation(self):
        # Test form with valid data
        form_data = {
            'username': 'employer1',
            'email': 'employer1@example.com',
            'password1': 'testpass12',
            'password2': 'testpass12',
            'CompanyName': 'Test Company',
            'employer_id': '12345',
            'is_employer': True,
            'bios': 'Test employer bio'
        }
        form = EmployerSignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test form with mismatched passwords
        form_data = {
            'username': 'employer1',
            'email': 'employer1@example.com',
            'password1': 'testpass',
            'password2': 'invalidpass',
            'CompanyName': 'Test Company',
            'employer_id': '12345',
            'is_employer': True,
            'bios': 'Test employer bio'
        }
        form = EmployerSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ["Passwords don't match"])
class CandidateSignUpFormTests(TestCase):
    def test_form_validation(self):
        # Test form with valid data
        form_data = {
            'username': 'candidate1',
            'email': 'candidate1@example.com',
            'password1': 'testpass12',
            'password2': 'testpass12',
            'first_name': 'Test',
            'last_name': 'Candidate',
            'candidate_id': '12345',
            'date_of_birth': '2000-01-01',
            'phone_number': '123-456-7890',
            'bios': 'Test candidate bio'
        }
        form = CandidateSignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test form with mismatched passwords
        form_data = {
            'username': 'candidate1',
            'email': 'candidate1@example.com',
            'password1': 'testpass',
            'password2': 'invalidpass',
            'first_name': 'Test',
            'last_name': 'Candidate',
            'candidate_id': '12345',
            'date_of_birth': '2000-01-01',
            'phone_number': '123-456-7890',
            'bios': 'Test candidate bio'
        }
        form = CandidateSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ["Passwords don't match"])

class CandidateFormTests(TestCase):
    def test_form_validation(self):
        # Test form with valid data
        form_data = {
            'first_name': 'Test',
            'last_name': 'Candidate',
            'date_of_birth': '2000-01-01',
            'phone_number': '123-456-7890',
            'bios': 'Test candidate bio'
        }
        form = CandidateForm(data=form_data)
        self.assertTrue(form.is_valid())

class EmployerFormTests(TestCase):
    def test_form_validation(self):
        # Test form with valid data
        form_data = {
            'CompanyName': 'Test Company',
            'employer_id': '12345',
            'bios': 'Test employer bio'
        }
        form = EmployerForm(data=form_data)
        self.assertTrue(form.is_valid())        