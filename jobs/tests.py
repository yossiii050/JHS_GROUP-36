
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

"""
import unittest
from django.test import RequestFactory
from .models import Upload
from .views import Upload_list
class UploadListTestCase(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Upload model
        self.upload = Upload.objects.create(
            title='Test Title',
            subTitle='Test Subtitle',
            body='Test body',
        )
    def test_applyCv(self):
        request = self.factory.post(reverse('jobs:applyCv', kwargs={'upload_id': self.job.slug}), {'username': self.user.username})
        request.user = self.user

    def test_upload_str(self):
        self.assertEqual(self.upload.title, 'Test Title')
        self.assertEqual(self.upload.subTitle, 'Test Subtitle')
        self.assertEqual(self.upload.body, 'Test body')