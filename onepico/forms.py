from django import forms
from django.forms import TextInput, NumberInput, EmailInput
from django.forms import TimeInput, DateInput, Textarea
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['name', 'last_name', 'party_size', 'prefix',
                  'phone', 'date', 'start_time', 'email', 'excerpt']
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and remove 
        auto-generated labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'Name': 'name',
            'Last name': 'last_name',
            'Party size': 'party_size',
            'Prefix': 'prefix',
            'Phone number': 'phone',
            'Date': 'date',
            'Time slot': 'start_time',
            'Email': 'email',
            'Booking comment': 'excerpt',
        }

        for filed in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'

        # for field in self.fields:
        #     if self.fields[field].required:
        #         placeholder = f'{placeholders[field]} *'
        #     else:
        #         placeholder = placeholders[field]
        #     # self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].label = False
