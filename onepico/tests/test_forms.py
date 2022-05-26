from django.test import TestCase
from .forms import *


class TestBookingForm(TestCase):

    def test_phone_is_required(self):
        """
        Test phone field is required
        """
        form = BookingForm({'phone': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'This field is required.')

    def test_excerpt_field_is_not_required(self):
        """
        Test excertp field is not required
        GIVES FAILURE, I DON'T KNOW WHY
        """
        form = BookingForm({'excerpt': ''})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_forms_metaclass(self):
        """
        Test fields are explicit in forms metaclass
        """
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['name', 'surname', 'people',
                                            'prefix', 'phone', 'date',
                                            'start_time', 'email', 'excerpt'])
