from django.test import TestCase
from django.urls import reverse
from polls.maintenance_middleware import MaintenanceMiddleware


class MaintenanceModeTestCase(TestCase):
    def test_maintenance_mode(self):
        # Set the maintenance_mode flag to True
        MaintenanceMiddleware.maintenance_mode = True

        # Send a request to the home page
        response = self.client.get(reverse('home page site'))

        # Verify that the response redirects to the maintenance page
        self.assertRedirects(response, reverse('maintenance'))

        # Send a request to the maintenance page
        response = self.client.get(reverse('maintenance'))

        # Verify that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Set the maintenance_mode flag to False
        MaintenanceMiddleware.maintenance_mode = False

        # Send a request to the home page
        response = self.client.get(reverse('home'))

        # Verify that the response status code is 200
        self.assertEqual(response.status_code, 200)