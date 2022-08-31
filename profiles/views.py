from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView, UpdateView

from django.urls import reverse_lazy

from django.contrib.auth.models import User
from onepico.models import Booking
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


class Profile(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            user_id = request.user.pk
            user = get_object_or_404(User, pk=user_id)

            profile = get_object_or_404(UserProfile, user=user)
            user_bookings = Booking.objects.filter(user_profile=profile).all()
            profile_form = UserProfileForm()
            context = {
                'user': user,
                'user_bookings': user_bookings,
                'profile_form': profile_form
            }
        return render(request, 'profiles/profile.html', context)


def delete_profile(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return render(request, 'account/account_delete_confirm.html')


class UpdateProfile(UpdateView):

    model = User
    fields  = ['first_name', 'last_name', 'email']
    success_url = 'profile'
    template_name = 'profile.html'


class BookingCancelation(DeleteView):

        model = Booking
        success_url = 'cancelation_confirmation'
        template_name = "cancelation_confirmation.html"