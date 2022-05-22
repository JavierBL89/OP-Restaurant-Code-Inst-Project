from django.test import TestCase
import unittest
from datetime import datetime
from .reservation import check_double_booking_week  

# Create your tests here.

class BookingAproved(unittest.TestCase):

    def test_check_double_booking_week(self):

        date = datetime.strptime('2022-11-11', '%Y-%m-%d')
        start_time = datetime.strptime('12:30', '%H:%M')
        self.assertFalse(check_double_booking_week('0', date, start_time, '123456789'))

if __name__ == '__main__':
    unittest.main()
