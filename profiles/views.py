from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView, UpdateView

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

