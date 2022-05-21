from django.test import TestCase
from .forms import *


# class Setup_Class(TestCase):

#     def setUp(self):

#         self.booking = Booking.objects.create(name='Veronica', surname='Leon', people=2, prefix='+353', phone=123456789, date=5/5/20022, start_time=12:30, email='notri80@gmail.com', excerpt='')


class TestBookingForm(TestCase):

    def test_phone_is_required(self):
        # form = BookingForm(data={'name': 'Veronica', 'surname': 'Leon', 'people': 2, 'prefix': '+353', 'phone':123456789, 'date': 5/5/20022, 'start_time': 12:30, 'email': 'notri80@gmail.com', 'excerpt': ''})
        form = BookingForm({'phone': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'This field is required.')


    def test_excerpt_field_is_not_required(self):
        form = BookingForm({'excerpt': ''})
        self.assertTrue(form.is_valid())


    def test_filds_are_explicit_in_forms_metaclass(self):
        form = BookingForm()

        self.assertEqual(form.Meta.fields, ['name', 'surname', 'people', 'prefix', 'phone', 'date', 'start_time', 'email', 'excerpt'])