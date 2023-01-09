from django.test import TestCase
from .models import Ticket
from .forms import TicketForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class TicketModelTest(TestCase):

   def setUp(self):
         self.user, created = get_user_model().objects.get_or_create(
         username='testuser',
         email='test@email.com',
         password='testpass12'
      )
         self.user1, created = get_user_model().objects.get_or_create(username='user1', password='testpass')
         self.user2, created = get_user_model().objects.get_or_create(username='user2', password='testpass')
         self.ticket = Ticket.objects.create(
         title='Test Ticket',
         body='This is a test ticket',
         user=self.user,
         handler=self.user,
         closed_by=self.user
      ) 

   def test_ticket_str(self):
         self.assertEqual(str(self.ticket), self.ticket.title)
      
   def test_ticket_handler(self):
         handler = get_user_model().objects.create_user(
               username='handler',
               email='handler@email.com',
               password='handlerpass12'
         )
         self.ticket.handler = handler
         self.ticket.save()
         self.assertEqual(self.ticket.handler, handler)

   def test_ticket_isopen(self):
         self.assertTrue(self.ticket.isopen)
         self.ticket.isopen = False
         self.ticket.save()
         self.assertFalse(self.ticket.isopen)

   def test_ticket_title(self):
         ticket = Ticket.objects.get(id=1)
         expected_object_name = f'{ticket.title}'
         self.assertEqual(expected_object_name, 'Test Ticket')
    
   def test_create_ticket(self):
         form_data = {'title': 'Test Ticket', 'body': 'This is a test ticket'}
         form = TicketForm(data=form_data)
         form.user = self.user
         ticket = form.save()
         self.assertEqual(ticket.title, 'Test Ticket')
         self.assertEqual(ticket.body, 'This is a test ticket')

   def test_view_status_code(self):
         url = '/create_ticket/'
         response = self.client.get(url)
         self.assertEqual(response.status_code, 404)


class TicketFormTest(TestCase):
    def test_form_validation(self):
        # Test form with all required fields
        form_data = {
            'title': 'Test Ticket',
            'body': 'This is a test ticket',
        }
        form = TicketForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Test form with missing required field
        form_data = {
            'title': '',
            'body': 'This is a test ticket',
        }
        form = TicketForm(data=form_data)
        self.assertFalse(form.is_valid())


class ViewTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(
            username='staff_user',
            email='staff@email.com',
            password='staffpass',
            is_staff=True
        )
        self.non_staff_user = User.objects.create_user(
            username='non_staff_user',
            email='non_staff@email.com',
            password='non_staffpass'
        )
        self.client.login(username='staff_user', password='staffpass')
        self.ticket = Ticket.objects.create(
            title='Test Ticket',
            body='This is a test ticket',
            user=self.staff_user
        )

    def test_techtickets_view(self):
        
        response = self.client.get(reverse('tech_tickets'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tech_tickets.html')
