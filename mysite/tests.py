from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from mysite.authentication import MyUserAuthBackend

class MyUserAuthBackendTest(TestCase):
    def setUp(self):
        self.backend = MyUserAuthBackend()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_authenticate_valid_user(self):
        authenticated_user = self.backend.authenticate(request=None,username='testuser', password='testpassword')

        self.assertEqual(authenticated_user, self.user)

    def test_authenticate_invalid_user(self):
        authenticated_user = self.backend.authenticate(request=None,username='testuser', password='wrongpassword')
        self.assertIsNone(authenticated_user)

    def test_authenticate_nonexistent_user(self):
        authenticated_user = self.backend.authenticate(request=None,username='nonexistentuser', password='testpassword')
        self.assertIsNone(authenticated_user)
