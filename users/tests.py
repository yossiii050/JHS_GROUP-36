from django.test import TestCase,Client
from django.contrib.auth import get_user_model,authenticate
from .models import Employer, Candidate,staffUser
from .forms import EmployerSignUpForm, CandidateSignUpForm, CandidateForm, EmployerForm
from users.models import Candidate,User,CVFormModel, FIELD_CHOICES, YEARS_CHOICES, EDUCATION_CHOICES
from django.urls import reverse
from users.views import ReportUsers
from django.http import HttpRequest
from django.contrib.auth.models import Group,User
from django.http import Http404
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
class ReportVIPUsersViewTests(TestCase):
    """"""  
    def test_view_only_accessible_to_staff(self):
        response = self.client.get(reverse('VipUsers'))
        self.assertEqual(response.status_code, 302)

        staff_user = User.objects.create_user(
            username='staff', password='password', is_staff=True)
        self.client.login(username='staff', password='password')



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


        self.assertEqual(employer.user.username, 'employer1')
        self.assertEqual(employer.email, 'employer1@example.com')
        self.assertEqual(employer.username, 'employer1')
        self.assertEqual(employer.CompanyName, 'Test Company')
        self.assertEqual(employer.employer_id, '12345')
        self.assertTrue(employer.is_employer)
        self.assertEqual(employer.bios, 'Test employer bio')

class CandidateModelTests(TestCase):
    def test_candidate_creation(self):

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

        form_data = {
            'CompanyName': 'Test Company',
            'employer_id': '12345',
            'bios': 'Test employer bio'
        }
        form = EmployerForm(data=form_data)
        self.assertTrue(form.is_valid())        

class EmployerRegPageTests(TestCase):
    def test_employer_registration(self):

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
        response = self.client.post(reverse('employer register'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employer.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='employer1').exists())
        self.assertTrue(Employer.objects.filter(user__username='employer1').exists())

class CandidateRegPageTests(TestCase):
    def test_candidate_registration(self):

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
        response = self.client.post(reverse('candidate register'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Candidate.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='candidate1').exists())
        self.assertTrue(Candidate.objects.filter(user__username='candidate1').exists())

class LoginPageTests(TestCase):
    def setUp(self):

        self.test_user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):

        form_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(reverse('login'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('home page')))

    def test_login_invalid_credentials(self):

        form_data = {
            'username': 'testuser',
            'password': 'invalidpass'
        }
        response = self.client.post(reverse('login'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username OR Password is incorrect')

class LogoutUserTests(TestCase):
    def setUp(self):

        self.test_user = User.objects.create_user(username='testuser', password='testpass')

    def test_logout(self):

        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('login')))        

class EditProfileTests(TestCase):
    def setUp(self):

        self.employer = User.objects.create_user(username='employer', password='testpass12')
        self.candidate = User.objects.create_user(username='candidate', password='testpass12')

    def test_employer_edit_profile(self):

        self.client.login(username='employer', password='testpass12')
        form_data = {
            'CompanyName': 'Test Company',
            'employer_id': '12345',
            'bios': 'Test employer bio'
        }

    def test_edit_profile_invalid_user(self):

        self.client.login(username='candidate', password='testpass')
        response = self.client.get(reverse('edit_profile', kwargs={'username': 'invalid'}))
        self.assertRaises(Http404)    

class DeleteAccountTests(TestCase):
    def setUp(self):

        self.test_user = User.objects.create_user(username='testuser', password='testpass12')

    def test_delete_account(self):

        self.client.login(username='testuser', password='testpass12')
        response = self.client.post(reverse('delete_account'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('home page')))
        self.assertFalse(User.objects.filter(username='testuser').exists())        

class ChangePassViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@test.com'
        )
        self.client.login(username='testuser', password='testpassword')
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pass_change.html')

    def test_view_redirects_on_post(self):
        response = self.client.post(reverse('change_password'), {
            'old_password': 'testpassword',
            'new_password1': 'newpassword',
            'new_password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 200)

class StaffUserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.staff_user = staffUser.objects.create(user=self.user, username='teststaff')

    def test_staff_user_created_successfully(self):
        self.assertEqual(staffUser.objects.count(), 1)
        self.assertEqual(staffUser.objects.first().username, 'teststaff')
        self.assertEqual(staffUser.objects.first().user, self.user)

    def test_set_password(self):
        self.staff_user.set_password('newpassword')
        self.staff_user.save()
        self.assertFalse(self.staff_user.user.check_password('newpassword'))

    def test_username_field(self):
        self.assertEqual(staffUser.USERNAME_FIELD, 'username')        


class CVFormModelTestCase(TestCase):
    def setUp(self):
        self.cv_form = CVFormModel.objects.create(
            field=FIELD_CHOICES[0][0],
            yearsexp=YEARS_CHOICES[0][0],
            education=EDUCATION_CHOICES[0][0],
            GitUrl='https://github.com/testuser',
            file=SimpleUploadedFile("file.pdf", b"file_content")
        )

    def test_cv_form_str(self):
        self.assertEqual(str(self.cv_form), 'https://github.com/testuser')
    
    def test_cv_form_file_upload(self):
        with open(self.cv_form.file.path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, b'file_content')

    def test_cv_form_field_validation(self):
        with self.assertRaises(ValidationError):
            self.cv_form.field = 'not a field'
            self.cv_form.full_clean()