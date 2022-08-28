from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """ Define contact form """
    
    class Meta:
        model = Contact
        contact_comment = forms.CharField(widget=forms.Textarea())

        fields = ('contact_name', 'contact_email', 'contact_comment',)

    def __init__(self, *args, **kwargs):
        """ Set autofocus and placeholders"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Your name',
            'contact_email': 'Your email address',
            'contact_comment': 'How can we help you?',
        }

        self.fields['contact_name'].widget.attrs['autofocus'] = True
        self.fields['contact_comment'].widget.attrs['cols'] = '40'
        self.fields['contact_comment'].widget.attrs['rows'] = '4'
        for field in self.fields:
            placeholder = placeholders
            self.fields[field].widget.attrs['class'] = 'contact-form-input'

            if self.fields[field].required:
                self.fields[field].widget.attrs['placeholder'] = f'{placeholder[field]} *'
