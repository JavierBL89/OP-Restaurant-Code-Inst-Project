from django.db import models

# Create your models here.

STATUS =  (
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('rejected', 'rejected'),
    ('expired', 'expired')
)


class Restaurant():
    """
    Class to define restaurant
    """
    opening_days = ["Tuesday","Wednesday","Thursday","Friday","Saturday"]
    opening_time= '12:00'
    closing_time = '21:30'
    small_table = [{'table': 1, 'max_px': 2}, {'table': 2, 'max_px': 2}, {'table': 3, 'max_px': 2},{'table': 4, 'max_px': 4}]
    medium_table = [{'table': 5, 'max_px': 4}, {'table': 6, 'max_px': 4}]
    large_table = [{'table': 7, 'max_px': 7}, {'table': 8, 'max_px': 7}]
 
class Booking(models.Model):
    """
    Model to define booking data collection
    """
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=50, unique=False, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    people = models.BigIntegerField(null=True)
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


class TableLunch(models.Model):
    """
    Model to define table booked data at lunch time collection
    """

    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE,
                             related_name="book_table_lunch")
    table_number = models.IntegerField(default=0)
    table_max_people = models.BigIntegerField(default=2)
    booked_for = models.BigIntegerField(blank=True)
    table_status = models.CharField(choices=STATUS, default='pending', max_length=50)
    customer_name = models.CharField(max_length=50, blank=True)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} {self.table_id} {self.date} {self.start_time} {self.created_on} {self.table_number} {self.table_max_people}'


class TableDinner(models.Model):
    """
    Model to define table booked data at dinner time collection
    """
    table_id = models.ForeignKey(Booking, on_delete=models.CASCADE,
                             related_name="book_table_dinner")
    table_number = models.IntegerField(default=0)
    table_max_people = models.BigIntegerField(default=2)
    booked_for = models.BigIntegerField(blank=True)
    table_status = models.CharField(choices=STATUS, default='pending', max_length=50)
    customer_name = models.CharField(max_length=50, blank=True)
    date = models.DateField('%Y-%m-%d')
    start_time = models.TimeField('%H:%M')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer_name} {self.table_id} {self.date} {self.start_time} {self.created_on} {self.table_number} {self.table_max_people}'

