"""
import unittest
from django.test import RequestFactory
from .models import Upload
from .views import Upload_list
class UploadListTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.upload1 = Upload.objects.create(
            title='Test_1', subTitle='Test Subtitle 1',
            slug='Test_1', body='Test Body 1',
        )
        self.upload2 = Upload.objects.create(
            title='Test_2', subTitle='Test Subtitle 2',
            slug='Test_2', body='Test Body 2',
        )

    def test_upload_list_view(self):
        request = self.factory.get('/uploads/')
        response = Upload_list(request)
        self.assertEqual(response.status_code, 200)

    def test_sort_upload_list_view_by_title_ascending(self):
        request = self.factory.post('/uploads/', {'sort_field': 'title', 'sort_order': 'ascending'})
        response = Upload_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['uploads'][0], self.upload1)
        self.assertEqual(response.context_data['uploads'][1], self.upload2)

    def test_sort_upload_list_view_by_title_descending(self):
        request = self.factory.post('/uploads/', {'sort_field': 'title', 'sort_order': 'descending'})
        response = Upload_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['uploads'][0], self.upload2)
        self.assertEqual(response.context_data['uploads'][1], self.upload1)
        
    def test_sort_upload_list_view_by_date_ascending(self):
        request = self.factory.post('/uploads/', {'sort_field': 'date', 'sort_order': 'ascending'})
        response = Upload_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['uploads'][0], self.upload1)
        self.assertEqual(response.context_data['uploads'][1], self.upload2)"""