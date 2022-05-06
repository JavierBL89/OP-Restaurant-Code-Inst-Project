from django.contrib import admin
from .models import Booking, TableLunch, TableDinner
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Booking)
class  PostAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'surname', 'created_on','id')
    list_filter = ('date', 'created_on', 'name', 'surname')
    search_fields = ['name', 'surname']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')


@admin.register(TableLunch, TableDinner)
class  PostTableLunchAdmin(SummernoteModelAdmin):
    
    list_display = ('customer_name', 'booked_for', 'table_max_people', 'start_time','date', 'id')
    list_filter = ('date', 'created_on', 'customer_name', 'table_max_people')
    search_fields = ['customer_name', 'table_max_people']
    summernote_fields = ('content')