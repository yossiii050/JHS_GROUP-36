from django.test import TestCase,RequestFactory
from django.urls import reverse
from users.models import Candidate, Employer
from jobs.forms import UploadForm
from django.contrib.auth.models import User
from jobs.models import Upload
from . import views

"""class UploadJobTest(TestCase):
#USER STORY 1
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

    def test_uploadJob_redirects_to_success(self):
        response = self.client.post(reverse('upload'), self.form_data)
        self.assertRedirects(response, reverse('success'))

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

"""   
