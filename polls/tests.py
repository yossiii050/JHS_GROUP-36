from django.test import TestCase
from django.urls import reverse
from polls.maintenance_middleware import MaintenanceMiddleware
from polls.views import toggle_maintenance_mode,maintenance
from django.contrib.auth.models import User

class MaintenanceViewTests(TestCase):
    def test_toggle_maintenance_mode(self):
        response = self.client.get(reverse('toggle_maintenance_mode'))
        self.assertRedirects(response, reverse('maintenance'))

    def test_maintenance_view(self):
        response = self.client.post(reverse('maintenance'), {'password': 'wrongpassword'})
        self.assertContains(response, 'Incorrect password')
        response = self.client.get(reverse('maintenance'))
        self.assertContains(response, 'Enter password')


    def test_maintenance_view_with_maintenance_mode_on(self):
        MaintenanceMiddleware.maintenance_mode = True
        response = self.client.post(reverse('maintenance'), {'password': 'wrongpassword'})
        self.assertContains(response, 'Incorrect password')
        response = self.client.get(reverse('maintenance'))
        self.assertContains(response, 'Enter password')

    def test_toggle_maintenance_mode_with_maintenance_mode_off(self):
        response = self.client.get(reverse('toggle_maintenance_mode'))
        self.assertRedirects(response, reverse('maintenance'))
        self.assertTrue(MaintenanceMiddleware.maintenance_mode)

    def test_toggle_maintenance_mode_with_maintenance_mode_on(self):
        MaintenanceMiddleware.maintenance_mode = True
        response = self.client.get(reverse('toggle_maintenance_mode'))
        self.assertRedirects(response, reverse('maintenance'))
        self.assertTrue(MaintenanceMiddleware.maintenance_mode)

    def test_maintenance_view_with_maintenance_mode_off_direct_access(self):
        response = self.client.get(reverse('maintenance'))
        self.assertEqual(response.status_code, 200)
    
    def test_toggle_maintenance_mode(request):
        # Test that the maintenance mode flag is set to True
        toggle_maintenance_mode(request)
        assert MaintenanceMiddleware.maintenance_mode == True
        
        # Test that the user is redirected to the maintenance page
        response = toggle_maintenance_mode(request)
        assert response.status_code == 302
        assert response.url == '/polls/maintenance/'


    