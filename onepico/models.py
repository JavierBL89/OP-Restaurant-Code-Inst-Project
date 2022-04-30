from django.db import models
from enum import Enum


# Create your models here.

STATUS = ((0, "draft"), (1, "booked"))
PREFIX = [
    ('+353'),
    ('+34'),
    ('+35'),
]


class Restaurant(Enum):
    table_for_2 = 4
    table_for_4 = 4
    table_for_6 = 4
    opening_time= '12:00'
    closing_time = '21:30'

    def __str__(self):
        return f"Table for 2, {self.table_for_2}, table for 4, {self.table_for_4}, table for 6, {self.table_for_6}"
    


class Booking(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BigIntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'


class Table(models.Model):
    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="book_table")
        
    def __str__(self):
        return f"Table_id {self.table_id}"