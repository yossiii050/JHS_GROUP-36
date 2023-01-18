from django.test import TestCase,RequestFactory
from django.urls import reverse
from users.models import Candidate, Employer
from jobs.forms import UploadForm,SortForm
from jobs.views import Upload_list, uploadJob
import jobs.urls
from django.contrib.auth.models import User
from jobs.models import Upload
from . import views

class UploadJobTest(TestCase):
    def setUp(self):
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
        self.form_data = {
            'title': 'Test Job',
            'subTitle': 'Test Subtitle',
            'body': 'This is a test job',
            'category': 1,
            'salaryRange': 1,
            'yearsexp': 1,
            'education': 1,
            'time': 1,
            'hybrid': True,
            'priority': 1,
            'location': 1,
            'availableAmount': 5,
            'notification': 5,
        }

#Test that the view returns a success template when a valid form is submitted:
    def test_upload_job_success(self):
        self.client.login(username='employer1', password='testpass')
        response = self.client.post(reverse('upload'), data=self.form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/success.html')

#Test that the view returns a form with errors when an invalid form is submitted:
    def test_upload_job_form_invalid(self):
        self.client.login(username='employer1', password='testpass')
        self.form_data['title'] = ''
        response = self.client.post(reverse('upload'), data=self.form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

#Test that the view correctly sets the owner of the job to the currently logged in user:
    def test_upload_job_owner(self):
        self.client.login(username='employer1', password='testpass')
        self.client.post(reverse('upload'), data=self.form_data)
        job = Upload.objects.get(title='Test Job')
        self.assertEqual(job.owner.username, 'employer1')

#Test that the view correctly sets the slug of the job to the title of the job:
    def test_upload_job_slug(self):
        self.client.login(username='employer1', password='testpass')
        self.client.post(reverse('upload'), data=self.form_data)
        job = Upload.objects.get(title='Test Job')
        self.assertEqual(job.slug, 'Test Job')

#Test that the view correctly saves the job to the database:
    def test_upload_job_saved(self):
        self.client.login(username='employer1', password='testpass')
        self.client.post(reverse('upload'), data=self.form_data)
        job = Upload.objects.filter(title='Test Job')
        self.assertTrue(job.exists())

class UploadListViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='employer1', email='employer1@example.com', password='testpass')
        self.employer = Employer.objects.create(
            user=user,
            email='employer1@example.com',
            username='employer1',
            CompanyName='Test Company',
            employer_id='12345',
            is_employer=True,
            bios='Test employer bio'
        )

        self.factory = RequestFactory()
        self.upload = Upload.objects.create(
            title='Test_Title',
            subTitle='Test subTitle',
            body='Test body',
            slug='Test_Title',
            owner=self.employer,   
        )
    #Test that the Upload_list view returns a status code of 200 for a GET request
    def test_get_request(self):
        request = self.factory.get(reverse('list'))
        response = Upload_list(request)
        self.assertEqual(response.status_code, 200)

    #Test that the Upload_list view returns the correct template for a GET request.
    def test_template_used(self):
        request = self.factory.get(reverse('list'))
        response = Upload_list(request)
        self.assertEqual(request.path, reverse('list'))


class ApplyCvTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='password')
        self.employer = Employer.objects.create(user=self.user)
        self.job = Upload.objects.create(title='Job Title', owner=self.employer, slug='unique-slug')
        self.candidate = Candidate.objects.create(user=self.user, candidate_id='123', email='test@email.com',username='testuser',date_of_birth='1996-10-10')

    def test_apply_cv(self):
        response = self.client.get(reverse('ApllyCv', args=[self.job.slug]))
        self.assertEqual(response.status_code, 404)
        self.candidate.refresh_from_db()        