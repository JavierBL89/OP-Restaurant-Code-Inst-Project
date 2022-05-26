from django.test import TestCase
from .models import Booking


class TestModels(TestCase):

    def test_booking_status_is_pending(self):
        booking = Booking.objects.create(name='Javier', surname='Leon',
                                         people='2', prefix='+353',
                                         phone='123456789',
                                         date='2022-11-11',
                                         start_time='12:30',
                                         email='notri80@gmail.com',
                                         excerpt='')
        self.assertTrue(booking.status == "pending")
