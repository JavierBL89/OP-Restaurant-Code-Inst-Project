from datetime import timedelta, datetime
import time
from .models import Restaurant, Booking



def get_table_available(people, requested_date, requested_time, booking_id):
    minutes_slot = 120
    delta = timedelta(seconds=60*minutes_slot)
    slotime = requested_time + delta
    print(requested_time)
    print(slotime)

    # converts date into a string and gets weekday name
    requested_date_str = datetime.strftime(requested_date, "%Y-%m-%d") 
    date_name_day = time.strftime('%A', time.strptime(requested_date_str, "%Y-%m-%d"))
    requested_time_str =  datetime.strftime(requested_time, "%H:%M") 
    people = people
    requested_date_str = requested_date_str
    requested_time_str = requested_time_str
    # table_list = Booking.objects.filter(status=booked)
    # check_time = Booking.objects.filter(start_time=booking_time)
    
    if date_name_day in Restaurant.opening_days:
        if requested_time_str > "12:00" and requested_time_str < "14:30":
            request = Booking.objects.filter(id=booking_id)
            check_lunch_time(request)
            for2 = Booking.objects.filter(people=2).values()
            # for t in for2:
            #     print(t['name'])
            if people == "2":
                print("BOOKED")
                return True
        
            else:
                print("PUTA")

                return False
        else: 
            raise Exception("Service hours, Lunch from 12:00pm to 14:30, Dinner, from 18:00pm to 21:30pm")

    else: 
        raise Exception("Day of the week do not coincidence with opening days")
    

def check_lunch_time(request):
    
    for value in request.values():
       people_requested = value['people']
       if people_requested == 1 or people_requested == 2:

        #    small_available = Lunch.objects.filter(people=)
           print("somos 2")




# table_of_2 = Table(Table.status, Table.table_id)

    # booking_date = Booking.date
    # start_time = Booking.start_time
