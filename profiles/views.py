from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.


class Profile(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            user_id = request.user.pk
            profile = get_object_or_404(User, pk=user_id)
            print(profile)
        context = {
            'profile': profile,
        }
        return render(request, 'profiles/profile.html', context)


def delete_profile(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return render(request, 'account/account_delete_confirm.html')