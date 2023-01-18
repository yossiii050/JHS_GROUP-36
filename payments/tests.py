from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.test import TestCase

class AddUserToVipGroupTest(TestCase):
    def test_add_user_to_vip_group(self):
        group = Group.objects.create(name='VIP')
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_user_to_vip_group'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(user.groups.filter(name='VIP').exists())

    def test_add_user_to_vip_group(self):
        group = Group.objects.create(name='VIP')
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        #response = self.client.post(reverse('paymentpage'))
        #self.assertEqual(response.status_code, 200)
        #self.assertTrue(user.groups.filter(name='VIP').exists())