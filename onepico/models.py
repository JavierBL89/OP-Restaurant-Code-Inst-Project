from django.db import models

# Create your models here.

STATUS =  (
    (0, "pending"),
    (1, "confirmed"),
    (2, "rejected"),
    (3, "expired")
)

PREFIX = (
    ('+353','+353'),
    ('+34', '+34'),
    ('+35', '+35'),
    )

class Restaurant():

    # tables = [
    #     {'table number': 1, 'px': 2, 'table_id': None},
    #     {'table number': 2, 'px': 2, 'table_id': None},
    #     {'table number': 3, 'px': 4, 'table_id': None},
    #     ]
    # minutes_slot = 90
    # delta = timedelta(seconds=60*minutes_slot)
             
    table_for_2 = 4
    table_for_4 = 1
    table_for_6 = 4
    opening_days = ["Tuesday","Wednesday","Thursday","Friday","Saturday"]
    opening_time= '12:00'
    closing_time = '21:30'

    def __str__(self):
        return f"Table for 2, {self.tables[0]}, table for 4, {self.tables[1]}, table for 6, {self.tables[2]}"
    

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
    status = models.IntegerField(choices=STATUS, default=0)
    

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time} {self.id}'


class Lunch(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    opening_time = models.TimeField('%H:%M')
    closing_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'

class Dinner(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    opening_time = models.TimeField('%H:%M')
    closing_time = models.TimeField('%H:%M')
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'



