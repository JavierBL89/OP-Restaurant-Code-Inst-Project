from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect
from datetime import datetime
from .reservation import  get_table_available,check_double_booking_date,check_double_booking_week
from django.contrib import messages



# Create your views here.

class HomePage(View):

    def get(self, request):

        form = BookingForm()
        context = {
            'form': form
        }

        return render(request, 'index.html', context)


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
            print("BOOKING CANCELED")
            print("BOOKING CANCELED PUTA")
            double_booking_day = True
            customer = Booking.objects.filter(phone=phone).all()
            double_booking_day = {
                'double_booking_day': double_booking_day,
                'customer': customer
            }
            return render(request, 'booking_confirmation.html', double_booking_day)
            
        elif check_double_booking_week(people, requested_date, requested_time, phone) == False:
            print("BOOKING CANCELED PUTA")

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
                return render(request, 'booking_confirmation.html', booking_successful)
            else:
                print("FULLY BOOKED")
        
        return render(request, 'index.html')


class BookingSearch(View):

    def get(self, request):
        return render(request, 'cancelations.html')


    def post(self, request, *args, **kawrgs):

        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date = request.POST.get('date')
        # requested_date = datetime.strptime(date, '%Y-%m-%d')

        customer_record = Booking.objects.filter(phone=phone, email=email, date=date)
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
        print("puta")
        template_name = "cancelations.html"

class CancelationConfirmation(View):

    def get(self, request):
        return render(request, 'cancelation_confirmation.html')











