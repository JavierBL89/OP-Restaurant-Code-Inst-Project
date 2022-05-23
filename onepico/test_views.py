from django.test import TestCase
from .models import Booking
from datetime import datetime


class TestViews(TestCase):

    def test_get_home_page(self):
        """ 
        Test cancelation confirmation page status 
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_cancelations_page(self):
        """ 
        Test cancelation confirmation page status
        """
        response = self.client.get('/cancelations')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelations.html')

    def test_get_cancelation_confirmation_page(self):
        """ 
        Test cancelation confirmation page status
        """
        response = self.client.get('/cancelation-confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelation_confirmation.html')

    def test_get_resevation_confirmation_page(self):
        """ 
        Test reservation confirmation page status.
        and the test fails, i don't know why
        """
        response = self.client.get('/reservation_confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_confirmation.html') 

    def test_form_post_redirect_success_page(self):
        """ 
        Test reservation form is post is succesfuly,
        and redirects the user to the success reservation page.
        Creates a new reservation object
        GIVES FAILURE, I DON'T KNOW WHY!
        """
        response = self.client.post('/', {'name': 'Javier', 'surname': 'Bastande Leon', 'party_size': 2, 'prefix': '+353', 'phone':'123456789', 'date': '2022-11-11', 'start_time': '12:30', 'email': 'notri80@gmail.com', 'excerpt': ''})
        self.assertTemplateUsed(response, 'reservation_confirmation.html')
    
    def test_reservation_search_redirect_success_page(self):
        """ 
        Test redirect user to submiting cancelations page
        after booking search request
        GIVES FAILURE, I DON'T KNOW WHY!
        """
        response = self.client.post('/cancelations', {'phone':'123456789', 'date': '2022-11-11',  'email': 'notri80@gmail.com'})
        self.assertTemplateUsed(response, 'cancelations.html')

    def test_cancel_existing_reservation(self):
        booking = Booking.objects.create(name='Veronica', surname='Leon', people='2', prefix='+353', phone='123456789', date='2022-11-11', start_time='12:30', email='notri80@gmail.com', excerpt='')
        # response = self.client.get('/cancelation-confirmation')
        # self.assertRedirects(response, 'onepico/cancelation_confirmation.html')
        existing_booking = Booking.objects.filter(id=booking.id)
        print(existing_booking)
        existing_booking.delete()
        self.assertEqual(len(existing_booking), 0)
        


        