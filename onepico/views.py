from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Booking
from .forms import BookingForm
from profiles.models import UserProfile
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from datetime import datetime
from .reservation import  get_table_available, check_double_booking_date
from django.contrib import messages


# Create your views here.

class HomePage(View):

    def get(self, request):
        form = BookingForm()
        contact_form = ContactForm()
        home = True
        context = {
            'form': form,
            'contact_form': contact_form,
            'home': home
        }

        return render(request, 'index.html', context)


class FormView(View):

    def get(self, request):
        return render(request, 'reservation_confirmation.html')


    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        surname = request.POST['last_name']
        prefix = request.POST['prefix']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        requested_date = datetime.strptime(date, '%Y-%m-%d')
        start_time = request.POST['start_time']
        format_data = "%H:%M"
        requested_time = datetime.strptime(start_time, format_data)
        people = request.POST['party_size']
        comment = None
        if 'booking_comments' in request.POST:
            comment = request.POST['booking_comments']

        
        if check_double_booking_date(people, requested_date, requested_time, phone) == False:
            print("BOOKING CANCELED!! DOUBLE BOOKING DAY")
            double_booking_day = True
            customer = Booking.objects.filter(phone=phone,date=requested_date).all()
            double_booking_day = {
                'double_booking_day': double_booking_day,
                'customer': customer
            }
            return render(request, 'reservation_confirmation.html', double_booking_day)
            
        else:
            # try:
            new_booking = Booking(name=name, last_name=surname, party_size=people, prefix=prefix, phone=phone, date=requested_date, start_time=requested_time, email=email, excerpt=comment)
            new_booking.save()
            booking_id = new_booking.id
            if get_table_available(people, requested_date, requested_time, booking_id) == True:

                if request.user.is_authenticated:
                    user_profile = get_object_or_404(UserProfile, user=request.user)
                    print('puta')
                    # Save info into user's account
                    user = get_object_or_404(User, pk=request.user.id)
                    user.first_name = name
                    user.last_name = surname
                    user.save()
                    # Attach booking to user's profile
                    new_booking.user_profile = user_profile
                    new_booking.save()
                    
                print("BOOKING SUCCESSFUL")
                booking_successful = True
                booking_successful = {
                'booking_successful': booking_successful
            }
                return render(request, 'reservation_confirmation.html', booking_successful)
            else:
                new_booking.delete()
                print("FULLY BOOKED")
                fully_booked = True
                fully_booked = {
                'fully_booked': fully_booked
            }
                return render(request, 'reservation_confirmation.html', fully_booked)
            # except Exception as e:
            #     print(f'Cannot make the request: Error{e}')
            #     return redirect(reverse('home'))

        
        return render(request, 'index.html')


class ResultsBookingSearch(View):
    def get(self, request):
            booking_search = True
            context = {
                'booking_search': booking_search
            }
            return render(request, 'cancel_request.html', context)


class BookingSearch(View):

    def get(self, request):
        cancelation = True
        context = {
            'cancelation': cancelation
        }
        return render(request, 'cancelations.html', context)

    def post(self, request, *args, **kawrgs):
        email = request.POST.get('reservation_email')
        date = request.POST.get('reservation_date')
        customer_record = Booking.objects.filter(email=email, date=date)
        if customer_record:
            customer_record = {
                'customer_record': customer_record
              }
            return render(request, 'cancelations.html', customer_record)             
        else:
              no_record = True
              no_record = {
                  "no_record": no_record
              }
              return render(request, 'cancelations.html', no_record)


class CancelationConfirmation(View):

    def get(self, request):
        return render(request, 'cancelation_confirmation.html')


class ReservationConfirmation(View):

    def get(self, request):
        return render(request, 'reservation_confirmation.html')











