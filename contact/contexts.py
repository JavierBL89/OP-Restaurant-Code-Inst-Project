from .forms import ContactForm
from django.conf import settings


def content(request):

    contact_form = ContactForm()
    maps_api_key = settings.MAPS_API_KEY


    context = {
        'contact_form': contact_form,
        'maps_api_key':  maps_api_key
    }
    
    return context
