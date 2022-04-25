from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Booking)
class  PostAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'surname', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['name', 'surname']
    summernote_fields = ('content')
