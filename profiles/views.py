from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
