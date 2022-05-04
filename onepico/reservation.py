from datetime import timedelta, datetime
import time
from .models import Restaurant, Booking



def get_table_available(people, date, start_time, booking_id):
    minutes_slot = 120
    delta = timedelta(seconds=60*minutes_slot)
    slotime = start_time + delta
    print(start_time)
    print(slotime)

    # converts date into a string and gets weekday name
    date = datetime.strftime(date, "%Y-%m-%d") 
    date = time.strftime('%A', time.strptime(date, "%Y-%m-%d"))
    start_time =  datetime.strftime(start_time, "%H:%M") 
    people = people
    date = date
    start_time = start_time
    # table_list = Booking.objects.filter(status=booked)
    # check_time = Booking.objects.filter(start_time=booking_time)
    
    # tables_booked= []
    if date in Restaurant.opening_days:
        if start_time > "12:00" and start_time < "14:30":
            for2 = Booking.objects.filter(people=2).count()
            if people == "2" and for2 <= 4  :
                print("BOOKED")
                print(for2)
                return True
        
            else:
                print("PUTA")
                print(for2)

                return False
        else: 
            raise Exception("Service hours, Lunch from 12:00pm to 14:30, Dinner, from 18:00pm to 21:30pm")

    else: 
        raise Exception("Day of the week do not coincidence with opening days")
    

# table_of_2 = Table(Table.status, Table.table_id)

    # booking_date = Booking.date
    # start_time = Booking.start_time
