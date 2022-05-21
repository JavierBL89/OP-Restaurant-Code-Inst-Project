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
        response = self.client.get('/cancelation confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelation_confirmation.html')


    
    def test_get_resevation_confirmation_page(self):
        """ 
        Test reservation confirmation page status.
        and the test fails, i don't know why
        """
        response = self.client.get('/reservation confirmation')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_confirmation.html') 


    def test_form_post_redirect_success_page(self):
        """ 
        Test reservation form is post is succesfuly,
        and redirects the user to the success reservation page
        """
        request = self.client.post('/reservation confirmation', {'name': '', 'surname': 'Leon', 'people': 2, 'prefix': '+353', 'phone':123456789, 'date': '2022/05/11', 'start_time': '12:30', 'email': 'notri80@gmail.com', 'excerpt': ''})
        self.assertRedirect(response, 'reservation_confirmation.html')
    
    def test_reservation_search_redirect_success_page(self):
        """ 
        Test redirect user to cancelations page
        after booking search request
        """
        request = self.client.post('/cancelations', {'phone':123456789, 'date': '5/5/20022',  'email': 'notri80@gmail.com'})
        self.assertRedirect(response, 'cancelations.html')
        