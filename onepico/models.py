from django.db import models
from enum import Enum


# Create your models here.

STATUS = ((0, "draft"), (1, "booked"))
PREFIX = [(
    ('+353'),
    ('+34'),
)]


class Room(Enum):
    for_two = 2
    for_three = 1
    for_four = 4


class Booking(models.Model):
    name = models.CharField(max_length=15, blank=True)
    surname = models.CharField(max_length=15, blank=True)
    people = models.IntegerField()
    prefix = models.IntegerField(choices=PREFIX, default=+353)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField(max_length = 100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    
    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.slot_time}'