
from django.contrib.auth.models import User
from django.test import TestCase,RequestFactory
from .models import Upload, Candidate
from .forms import UploadForm
from users.models import Employer
from django.shortcuts import get_object_or_404
from django.urls import reverse
from jobs.views import applyCv

#class UploadTestCase(TestCase):
#    def setUp(self):
#        # Create an instance of the Upload model
#        self.upload = Upload.objects.create(
#            title='Test Title',
#            subTitle='Test Subtitle',
#            body='Test body',
#        )

#    def test_upload_str(self):
#        self.assertEqual(self.upload.title, 'Test Title')
#        self.assertEqual(self.upload.subTitle, 'Test Subtitle')
#        self.assertEqual(self.upload.body, 'Test body')

class ApplyCvTest(TestCase):

    def setUp(self):
        # Create a user, a job and a candidate
        self.factory = RequestFactory()
        self.job = Upload.objects.create(title='Test Job', slug='test-job')
        self.user = User.objects.create_user(
            username='candidate1', email='candidate1@example.com', password='testpass'
        )
        self.candidate = Candidate.objects.create(
            user=self.user,
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
    def test_applyCv(self):
        request = self.factory.post(reverse('jobs:applyCv', kwargs={'upload_id': self.job.slug}), {'username': self.user.username})
        request.user = self.user
