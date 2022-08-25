from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect
from datetime import datetime
from .reservation import  get_table_available, check_double_booking_date
from django.contrib import messages


# Create your views here.

class HomePage(View):

    def get(self, request):

        form = BookingForm()
        home = True
        context = {
            'form': form,
            'home': home
        }

        return render(request, 'index.html', context)


class FormView(View):

    def get(self, request):
        return render(request, 'reservation_confirmation.html')


    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        surname = request.POST.get('l_name')
        prefix = request.POST.get('prefix')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        requested_date = datetime.strptime(date, '%Y-%m-%d')
        start_time = request.POST.get('start_time')
        format_data = "%H:%M"
        requested_time = datetime.strptime(start_time, format_data)
        people = request.POST.get('party_size')
        comment = request.POST.get('booking_comments')

        
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
            new_booking = Booking(name=name, surname=surname, people=people, prefix=prefix, phone=phone, date=requested_date, start_time=requested_time, email=email, excerpt=comment)
            new_booking.save()
            booking_id = new_booking.id
            if get_table_available(people, requested_date, requested_time, booking_id) == False:
                customer = Booking.objects.filter()
                print("BOOKING SUCCESSFUL")
                booking_successful = True
                booking_successful = {
                'booking_successful': booking_successful
            }
                return render(request, 'reservation_confirmation.html', booking_successful)
            else:
                print("FULLY BOOKED")
        
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

    

class BookingCancelation(DeleteView):

        model = Booking
        success_url = reverse_lazy('cancelation_confirmation')
        template_name = "cancelations.html"


class CancelationConfirmation(View):

    def get(self, request):
        return render(request, 'cancelation_confirmation.html')


class ReservationConfirmation(View):

    def get(self, request):
        return render(request, 'reservation_confirmation.html')











