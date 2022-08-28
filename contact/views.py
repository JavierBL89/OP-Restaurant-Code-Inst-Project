from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.core.mail import send_mail
from .send_email import send_contact_email

from onepico.forms import BookingForm
from .models import Contact
from .forms import ContactForm
# Create your views here.


class Contact(View):

    def post(self, request, *args, **kwargs):

        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_comment = request.POST['contact_comment']
        
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            send_contact_email(contact_name, contact_email, contact_comment)

        form = BookingForm()
        contact_form = ContactForm()
        home = True
        context = {
            'form': form,
            'contact_form': contact_form,
            'home': home
        }

        return render(request, 'index.html', context)

        return redirect(reverse('home/index'))

