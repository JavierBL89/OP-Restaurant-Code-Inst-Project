from django.contrib import admin
from .models import Booking, Lunch, Dinner
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Booking, Lunch, Dinner)
class  PostAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'surname', 'created_on')
    list_filter = ('date', 'created_on', 'name', 'surname')
    search_fields = ['name', 'surname']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')
