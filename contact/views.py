from django.shortcuts import render
from django.views import generic, View

# Create your views here.


class Contact(View):

    def post(self, *args, **kwargs):

        return render(request, 'index.html')

