from django.db import models
from profiles.models import UserProfile


# Create your models here.

STATUS = (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('rejected', 'rejected'),
    ('expired', 'expired')
)

PREFIX_CHOICES = [
    ('+34', '+34'),
    ('+353', '+353'),
    ('+44', '+44'),
]

TIME_SLOTS = [(' ', 'Lunch'),
              ('12:00', '12:00'), ('12:15', '12:15'),
              ('12:30', '12:30'), ('12:45', '12:45'),
              ('13:00', '13:00'), ('13:15', '13:15'),
              ('13:30', '13:30'), ('13:45', '13:45'),
              ('14:00', '14:00'), ('14:15', '14:15'),
              ('14:30', '14:30'),
              (' ', 'Dinner'),
              ('18:00', '18:00'),
              ('18:00', '18:00'), ('18:15', '18:15'),
              ('18:30', '18:30'), ('18:45', '18:45'),
              ('19:00', '19:00'), ('19:15', '19:15'),
              ('19:30', '19:30'), ('19:45', '19:45'),
              ('19:30', '19:30'), ('19:45', '19:45'),
              ('20:00', '20:00'), ('20:15', '20:15'),
              ('20:30', '20:30'), ('20:45', '20:45'),
              ('21:00', '21:00'), ('21:15', '21:15'),
              ('21:30', '21:30'),
]


class Restaurant():
    """
    Class to define restaurant
    """
    opening_days = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    opening_time = '12:00'
    closing_time = '21:30'
    small_table = [{'table': 1, 'max_px': 2}, {'table': 2, 'max_px': 2},
                   {'table': 3, 'max_px': 2}, {'table': 4, 'max_px': 4}]
    medium_table = [{'table': 5, 'max_px': 4}, {'table': 6, 'max_px': 4}]
    large_table = [{'table': 7, 'max_px': 7}, {'table': 8, 'max_px': 7}]


class Booking(models.Model):
    """
    Model to define booking data collection
    """
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.SET_NULL,
                                     blank=True, null=True,
                                     related_name='bookings')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    last_name = models.CharField(max_length=30, null=True)
    party_size = models.BigIntegerField(null=True)
    prefix = models.BigIntegerField(default=+353, choices=PREFIX_CHOICES)
    phone = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M', choices=TIME_SLOTS, default='12:00')
    email = models.EmailField(max_length=100)
    excerpt = models.TextField(null=True, blank=True, max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='pending', max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name} {self.party_size}'
        f'{self.date} {self.start_time} {self.id}' 


class TableLunch(models.Model):
    """
    Model to define table booked data at lunch time collection
    """

    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                 related_name="book_table_lunch")
    table_number = models.IntegerField(default=0)
    table_max_people = models.BigIntegerField(default=2)
    booked_for = models.BigIntegerField(blank=True)
    table_status = models.CharField(choices=STATUS,
                                    default='pending', max_length=50)
    customer_name = models.CharField(max_length=50, blank=True)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} {self.table_id} {self.date}'
        f'{self.start_time} {self.created_on}'
        f'{self.table_number} {self.table_max_people}'


class TableDinner(models.Model):
    """
    Model to define table booked data at dinner time collection
    """
    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE,
                                 related_name="book_table_dinner")
    table_number = models.IntegerField(default=0)
    table_max_people = models.BigIntegerField(default=2)
    booked_for = models.BigIntegerField(blank=True)
    table_status = models.CharField(choices=STATUS,
                                    default='pending', max_length=50)
    customer_name = models.CharField(max_length=50, blank=True)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} {self.table_id} {self.date}'
        f'{self.start_time} {self.created_on}'
        f'{self.table_number} {self.table_max_people}'



