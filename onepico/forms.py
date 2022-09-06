from django import forms
from django.forms import TextInput, NumberInput, EmailInput
from django.forms import TimeInput, DateInput, Textarea
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        date = forms.DateInput()
        excerpt = forms.CharField(widget=forms.Textarea())
        fields = ['name', 'last_name', 'party_size', 'prefix',
                  'phone', 'date', 'start_time', 'email', 'excerpt']
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and remove 
        auto-generated labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'last_name': 'Last name',
            'party_size': 'Party size',
            'prefix': '',
            'phone': 'Phone number',
            'date': 'Date',
            'start_time': 'Time slot',
            'email': 'Email',
            'excerpt': 'Booking comment',
        }

        self.fields['excerpt'].widget.attrs['cols'] = '40'
        self.fields['excerpt'].widget.attrs['rows'] = '2'
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class CancelBooking(forms.ModelForm):
    """ Bookings cancelation form """

    email = forms.EmailField(max_length=240)
    booking_date = forms.DateField()
    fields = ('email', 'booking_date')

    def __init__(self, *args, **kwargs):
        """ Set placeholders and get rid of labels """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email address',
            'date': 'Date',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False




       
