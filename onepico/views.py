from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect
from datetime import datetime



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
        date = datetime.strptime(date, '%Y-%m-%d')
        start_time = request.POST.get('start_time')
        start_time = datetime.strptime(start_time, '%H:%M')
        
        people = request.POST.get('party_size')
        comment = request.POST.get('booking_comments')

        Booking.objects.create(name=name, surname=surname, people=people, prefix=prefix, phone=phone, date=date, start_time=start_time, email=email, excerpt=comment)

        return render(request, 'index.html')


# class BookTable(View):
    
#     def post(self,request, *args, **kwargs):
        