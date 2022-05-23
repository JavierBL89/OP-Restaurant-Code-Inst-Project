from django.test import TestCase
import unittest
from datetime import datetime
from .reservation import check_double_booking_week
from .models import Booking

# Create your tests here.

class BookingAproved(unittest.TestCase):

    def test_check_double_booking_week(self):
        
        booking = Booking.objects.create(name='Veronica', surname='Leon', people='2', prefix='+353', phone='123456789', date='2022-11-11', start_time='12:30', email='notri80@gmail.com', excerpt='') 
        date = datetime.strptime('2022-11-11', '%Y-%m-%d')
        start_time = datetime.strptime('12:30', '%H:%M')
        existing_record = Booking.objects.filter(date=date, phone='123456789')
        # print(existing_record)
        self.assertTrue(len(existing_record) > 0)
        existing_record.delete()

        # self.assertFalse(check_double_booking_week('0', date, start_time, '123456789'))

if __name__ == '__main__':
    unittest.main()
