from django.db import models
from enum import Enum


# Create your models here.

STATUS = ((0, "draft"), (1, "booked"))
# PREFIX = [
#     ('+353'),
#     ('+34'),
#     ('+35'),
# ]


class Room(Enum):
    for_two = 2
    for_three = 1
    for_four = 4


class Booking(models.Model):
    # booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    people = models.BigIntegerField()
    prefix = models.BigIntegerField()
    phone = models.BigIntegerField(null=False, blank=False)
    date = models.DateField()
    start_time = models.TimeField()
    email = models.EmailField(max_length = 100)
    excerpt = models.CharField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BigIntegerField(choices=STATUS, default=0)

    
    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.start_time}'