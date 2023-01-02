from django.test import TestCase
from .models import Upload

class UploadModelTestCase(TestCase):
    def setUp(self):
        # Create a new Upload object
        self.upload = Upload.objects.create(
            title='TestTitle',
            subTitle='Test Subtitle',
            slug='test-slug',
            body='Test body',
            category=1,
            salaryRange=1,
            yearsexp=1,
            education='Test education',
            time=1,
            hybrid=True
        )

    def test_upload_str(self):
        self.assertEqual(str(self.upload), self.upload.title)

    def test_upload_snippet(self):
        self.assertEqual(self.upload.snippet(), 'Test body...')

    def test_upload_title_max_length(self):
        self.assertEqual(self.upload._meta.get_field('title').max_length, 60)

    def test_upload_subtitle_max_length(self):
        self.assertEqual(self.upload._meta.get_field('subTitle').max_length, 100)

    def test_upload_body_max_length(self):
        self.assertEqual(self.upload._meta.get_field('body').max_length, 200)

    def test_upload_education_max_length(self):
        self.assertEqual(self.upload._meta.get_field('education').max_length, 60)

