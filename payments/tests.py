from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse


class AddUserToVipGroupTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_paymentpage(self):
        # Make a GET request to the view
        response = self.client.get('/paymentpage/')
        
        
        # Assert that the user is now in the VIP group
        vip_group = Group.objects.get(name='VIP')
        self.assertIn(self.user, vip_group.user_set.all())
        
        # Assert that the correct template was used
        self.assertTemplateUsed(response, 'paymentview.html')
        
    def test_paymentpage_group_does_not_exist(self):
        # Delete the VIP group
        Group.objects.filter(name='VIP').delete()
        

'''

class DonateTest(TestCase):

    def setUp(self):
        self.client = Client()
        #group = Group.objects.create(name='VIP')
        #group.save()

    def test_donate_page(self):
        response = self.client.get('/paymentspage/')
        #response = self.client.get(reverse('paymentpage'))
        
        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered HTML contains the expected text
        self.assertContains(response, 'DONATE')
        self.assertContains(response, 'amount: { value: 88.44')
    '''