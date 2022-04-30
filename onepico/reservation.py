from datetime import timedelta
from .models import Restaurant, Booking, Table



def get_table_available(people, date, start_time):
    
    for_2 = 0
    for_4= Restaurant.table_for_4
    for_6= Restaurant.table_for_6
    people = people
    date = date
    start_time = start_time
    # table_list = Booking.objects.filter(status=booked)
    # check_time = Booking.objects.filter(start_time=booking_time)
    
    # tables_booked= []
    if people == "2" and for_2 > 0:
        print("BOOKED")
        return True
    
    else:
        print("PUTA")
        print(people)
        return False


    # booking_date = Booking.date
    # start_time = Booking.start_time
