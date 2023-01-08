

from django.test import TestCase
from .models import Upload
from .forms import UploadForm

class UploadTestCase(TestCase):
    def setUp(self):
        # Create an instance of the Upload model
        self.upload = Upload.objects.create(
            title='Test Title',
            subTitle='Test Subtitle',
            body='Test body',
        )

    def test_upload_str(self):
        self.assertEqual(self.upload.title, 'Test Title')
        self.assertEqual(self.upload.subTitle, 'Test Subtitle')
        self.assertEqual(self.upload.body, 'Test body')