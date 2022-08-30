from .forms import ContactForm


def content(request):

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form

    }
    
    return context
