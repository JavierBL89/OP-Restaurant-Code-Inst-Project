from datetime import timedelta, datetime
import time
from .models import Restaurant, Booking, Table



def get_table_available(people, date, start_time, booking_id):
    # converts date into a string and gets weekday name
    date = datetime.strftime(date, "%Y-%m-%d") 
    date = time.strftime('%A', time.strptime(date, "%Y-%m-%d"))

    start_time =  datetime.strftime(start_time, "%H:%M") 
    for_4= Restaurant.table_for_4
    for_6= Restaurant.table_for_6
    people = people
    date = date
    start_time = start_time
    # table_list = Booking.objects.filter(status=booked)
    # check_time = Booking.objects.filter(start_time=booking_time)
    minutes_slot = 90
    delta = timedelta(minutes=60)
    slot_time = start_time + delta
             
    # tables_booked= []
    if date in Restaurant.opening_days:
        if start_time > "12:00" and start_time < "14:30":
            for2 = Booking.objects.filter(people=2, leave_time=slot_time<"14:30" ).count()
            if people == "2" and for2 <= 4  :
                print("BOOKED")
                print(for2)
                return True
        
            else:
                print("PUTA")
                print(people)
                return False
        else: 
            raise Exception("Service hours, Lunch from 12:00pm to 14:30, Dinner, from 18:00pm to 21:30pm")

    else: 
        raise Exception("Day of the week do not coincidence with opening days")
        
    

table_of_2 = Table(Table.status, Table.table_id)

    # booking_date = Booking.date
    # start_time = Booking.start_time
