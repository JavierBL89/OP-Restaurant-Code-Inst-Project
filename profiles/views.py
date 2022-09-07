from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView, UpdateView
from datetime import date

from django.urls import reverse_lazy

from django.contrib.auth.models import User
from onepico.models import Booking
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class Profile(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            next_comming_bookings = []
            current_date = date.today()
            user_id = request.user.pk
            user = get_object_or_404(User, pk=user_id)
            profile = get_object_or_404(UserProfile, user=user)
            # attached possible bookings made as incognito to the new user
            user_bookings_non_attached = Booking.objects.filter(email=user.email).all()
            print(user_bookings_non_attached)

            for booking in user_bookings_non_attached:
                booking.user_profile = profile
                booking.save()
            # get bookings already attached to the user
            user_records = Booking.objects.filter(user_profile=profile).all()

            # get user bookings from the current day onwards
            for record in user_records:
                if record.date >= current_date:
                    next_comming_bookings.append(record)

            profile_form = UserProfileForm()
            context = {
                'user': user,
                'next_comming_bookings': next_comming_bookings,
                'profile_form': profile_form
            }
        else:
            return redirect(reverse('home'))
        return render(request, 'profiles/profile.html', context)


def delete_profile(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return render(request, 'account/account_delete_confirm.html')


class UpdateConfirmation(View):

    def get(self, request):

        if request.user.is_authenticated:
            return render(request, 'profiles/update_confirmation.html')
        else:
            return redirect(reverse('home'))


class CancelationConfirmation(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            return render(request, 'profiles/cancelation_confirmation.html')
        else:
            return redirect(reverse('home'))


class UpdateProfile(UpdateView):

    model = User
    fields  = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('update_confirmation')
    template_name = 'profiles/update_confirmation.html'


class BookingCancelation(DeleteView):

    model = Booking
    success_url = reverse_lazy('cancelation_confirmation')
    template_name = "profiles/cancelation_confirmation.html"

