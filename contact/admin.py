from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Class to show contact fields in admin panel
    """
    readonly_fields = ('contact_name', 'contact_email', 'contact_comment',)
    fields = ('contact_name', 'contact_email', 'contact_comment',)

    list_display = ('contact_name', 'contact_email')
