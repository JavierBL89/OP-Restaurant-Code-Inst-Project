from django.db import models

# Create your models here.

STATUS =  (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('rejected', 'rejected'),
    ('expired', 'expired')
)

PREFIX = (
    ('+353','+353'),
    ('+34', '+34'),
    ('+35', '+35'),
    )

class Restaurant():
             
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
    status = models.CharField(choices=STATUS, default='pending', max_length=50)
    

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
    status = models.CharField(choices=STATUS, default='pending', max_length=50)

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
    status = models.CharField(choices=STATUS, default='pending', max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'


class Table(models.Model):

    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE,
                             related_name="book_table")
    table_number = models.IntegerField(default=0)
    table_max_people = models.BigIntegerField(default=2)
    booked_for = models.BigIntegerField(blank=True)
    table_status = models.CharField(choices=STATUS, default='pending', max_length=50)
    customer_name = models.CharField(max_length=50, blank=True)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    created_on = models.DateTimeField(auto_now_add=True)

