from datetime import timedelta, datetime
import time
from .models import Restaurant, Booking, TableLunch, TableDinner
import random


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
    
    if date_name_day in Restaurant.opening_days:
        request = Booking.objects.filter(id=booking_id)
        # loop through the requested booking objectand get values
        for value in request.values():
           people_requested = value['people']
           booking_id = value['id']
           customer_name = value['name']
           date = value['date']
           people= value['people']
           start_time = value['start_time']

        if requested_time_str > "12:00" and requested_time_str < "14:30":
            if check_lunch_time(people_requested, booking_id, customer_name, date, people, start_time):
            # for2 = Booking.objects.filter(people=2).values()
                print("BOOKED")
                return True
        
            else:
                print("REJECTED")
                return False
        else: 
            raise Exception("Service hours, Lunch from 12:00pm to 14:30, Dinner, from 18:00pm to 21:30pm")

    else: 
        raise Exception("Day of the week do not coincidence with opening days")
    

def check_lunch_time(people_requested, booking_id, customer_name, date, people, start_time):
    tables_booked = [1,2,3]
    
    # get Booking instance to pass it into the new_table object as table_id value
    booking_id = Booking.objects.get(id=booking_id)
     
    if people_requested == 1 or people_requested == 2:
             random_table_object = random.choice(Restaurant.small_table)
             table_number = random_table_object.get('table')
              
             while True:
                 random_table_object = random.choice(Restaurant.small_table)
                 table_number= random_table_object.get('table')
                 table_max_people= random_table_object.get('max_px')
                 
                 if table_number in tables_booked:
                     print("Table number" ,table_number,  "booked")
                     check_lunch_time(request)
                     return True

                 elif len(tables_booked) > 3:
                     print("tables length", len(tables_booked))
                     print("tables booked", tables_booked)
                     print("FULLY BOOKED")
                     return True

                 elif table_number not in tables_booked:
                    tables_booked.append(table_number) 
                    new_table = TableLunch.objects.create(table_id=booking_id,table_number=table_number,booked_for=people, table_max_people=table_max_people,table_status='confirmed',customer_name=customer_name,date=date,start_time=start_time )
                    #   print(new_table)
                    print("Table number" ,table_number, " now booked")
                    print("tables length", len(tables_booked))
                    print("tables booked", tables_booked)
                    return False
                                  

                       
               


