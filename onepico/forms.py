from django import forms
from django.forms import TextInput, NumberInput, EmailInput
from django.forms import TimeInput, DateInput, Textarea
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['name', 'surname', 'people', 'prefix',
                  'phone', 'date', 'start_time', 'email', 'excerpt']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'label': "none",
                'placeholder': 'Name'
                }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Last name'
                }),
            'people': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Party size'
                }),
            'prefix': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Prefix'
                }),
            'phone': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Contact number'
                }),
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': 'mm/dd/yyyy'
                }),
            'start_time': TimeInput(attrs={
                'class': "form-control",
                'placeholder': 'Date'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }),
            'excerpt': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Booking comment'
                }),
        }
