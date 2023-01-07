from django.test import TestCase
from .models import Ticket
from .forms import TicketForm
class TicketModelTest(TestCase):

    def setUp(self):
        Ticket.objects.create(title='Test Ticket', body='This is a test ticket')

    def test_ticket_title(self):
        ticket = Ticket.objects.get(id=1)
        expected_object_name = f'{ticket.title}'
        self.assertEqual(expected_object_name, 'Test Ticket')
    
    def test_form_valid_input(self):
       form_data = {'title': 'Test Ticket', 'body': 'This is a test ticket'}
       form = TicketForm(data=form_data)
       self.assertTrue(form.is_valid())

    def test_form_invalid_input(self):
       form_data = {'title': '', 'body': ''}
       form = TicketForm(data=form_data)
       self.assertFalse(form.is_valid())
    
    def test_create_ticket(self):
       form_data = {'title': 'Test Ticket', 'body': 'This is a test ticket'}
       form = TicketForm(data=form_data)
       ticket = form.save()
       self.assertEqual(ticket.title, 'Test Ticket')
       self.assertEqual(ticket.body, 'This is a test ticket')
    
    def test_view_status_code(self):
       url = '/create_ticket/'
       response = self.client.get(url)
       self.assertEqual(response.status_code, 404)