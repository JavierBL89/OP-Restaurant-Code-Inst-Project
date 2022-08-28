from django.shortcuts import render
from django.views import generic, View

# Create your views here.


class Profile(View):

    def get(self, request):
        context = {}
        return render(request, 'profiles/profile.html', context)
