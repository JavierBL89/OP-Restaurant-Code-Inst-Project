from django.db import models
from enum import enum

# Create your models here.

STATUS = ((0, "failed"), (1, "booked"))

class Room(enum):
    for_two = 2
    for_three = 1
    for_four = 4

class Booking(model.Models):
    name = models.CharField(max_length=15, min_length=2, blank=True)
    surname = models.CharField(max_length=15, min_length=2, blank=True)
    people = models.IntegerField()
    phone = models.IntegerField()
    date = models.DateTimeField()
    time = 
    email = models.EmailField(max_length = 100)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choises=STATUS, default=0)
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.people} {self.date} {self.slot_time}'