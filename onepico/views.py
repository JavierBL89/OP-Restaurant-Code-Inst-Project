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
from django.conf import settings
from datetime import datetime
from .reservation import  get_table_available, check_double_booking_date
from django.contrib import messages


# Create your views here.

class HomePage(View):

    def get(self, request):
        form = BookingForm()
        contact_form = ContactForm()
        home = True
        maps_api_key = settings.MAPS_API_KEY
        context = {
            'form': form,
            'contact_form': contact_form,
            'maps_api_key': maps_api_key,
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
                # else:
                #     # attached possible bookings made as incognito to the new user
                #     existing_user_booking = Booking.objects.filter(email=user.email).all()
                #     user_bookings_non_attached.user_profile = profile
                #     user_bookings_non_attached.save()

                    
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


class ReservationConfirmation(View):

    def get(self, request):
        return render(request, 'reservation_confirmation.html')











