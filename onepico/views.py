from django.shortcuts import render
from django.views import generic, View

# Create your views here.

class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


class BookTable(View):
    pass