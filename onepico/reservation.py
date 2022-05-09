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
                print("Room fully booked for the date requested, try at another date")
                return True
        
            else:
                print("BOOKED")
                return False
        else: 
            raise Exception("Service hours, Lunch from 12:00pm to 14:30, Dinner, from 18:00pm to 21:30pm")

    else: 
        raise Exception("Day of the week do not coincidence with opening days")
    

def check_lunch_time(people_requested, booking_id, customer_name, date, people, start_time):
    
    # get Booking instance to pass it into the new_table object as table_id value
    booking_id = Booking.objects.get(id=booking_id)
     
    if people_requested == 1 or people_requested == 2:
        check_small_tables_available(people_requested, booking_id, customer_name, date, people, start_time)
    elif people_requested == 3 or people_requested == 4:
        check_medium_tables_available(people_requested, booking_id, customer_name, date, people, start_time)
    elif people_requested >= 5 or people_requested <= 7:
        check_large_tables_available(people_requested, booking_id, customer_name, date, people, start_time)
                                       

def check_small_tables_available(people_requested, booking_id, customer_name, date, people, start_time): 
    small_tables_booked_list = []
    while True:
        random_table_object = random.choice(Restaurant.small_table)
        table_number = random_table_object.get('table')
        table_max_people= random_table_object.get('max_px')
        
        tables_booked_requested_date = TableLunch.objects.filter(date=date).all()
        # loop through tables booked for requested day and get table number and start time
        for table in tables_booked_requested_date.values():
            table_number_booked = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time').strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str 
            service_finishing_time = "14:30"
            print("Print one table number for every loop and push it into tables booked", table_number_booked, "table start time", table.get('start_time') ) 
            if booked_tables_start_time_str <= service_finishing_time:
                if table_number_booked <= 4 and table_number_booked not in small_tables_booked_list:
                    small_tables_booked_list.append(table_number_booked) 
                    print("List small tables booked", small_tables_booked_list)
              
        if table_number in small_tables_booked_list and len(small_tables_booked_list) < 4:
            print("Table number" ,table_number,  "already booked")
            continue 
        elif len(small_tables_booked_list) >= 4:
            print("tables length", len(small_tables_booked_list))
            print("tables booked", small_tables_booked_list)
            print("SMALL TABLES FULLY BOOKED")
            if check_medium_tables_available(people_requested, booking_id, customer_name, date, people, start_time):
                return False
        elif table_number not in small_tables_booked_list:
           new_table = TableLunch.objects.create(table_id=booking_id,table_number=table_number,booked_for=people, table_max_people=table_max_people,table_status='confirmed',customer_name=customer_name,date=date,start_time=start_time )
           small_tables_booked_list.append(table_number)
           print("Table number" ,table_number, " now booked")
           print("tables length", len(small_tables_booked_list))
           print("print tables in list", small_tables_booked_list)
           print("tables booked", small_tables_booked_list)
           return True


def check_medium_tables_available(people_requested, booking_id, customer_name, date, people, start_time):
    medium_tables_booked_list = []
    while True:
        random_table_object = random.choice(Restaurant.medium_table)
        table_number= random_table_object.get('table')
        table_max_people= random_table_object.get('max_px')

        tables_booked_requested_date = TableLunch.objects.filter(date=date).all()
        # loop through tables booked for requested day and get table number and start time
        for table in tables_booked_requested_date.values():
            table = table.get('table_number')
            print("Print one table number for every search and push it into tables booked", table) 
            booked_tables_start_time_str = table.get('start_time').strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str 
            service_finishing_time = "14:30"
            print("Print one table number for every loop and push it into tables booked", table_number_booked, "table start time", table.get('start_time') ) 
            if booked_tables_start_time_str <= service_finishing_time:
                if table_number_booked >= 5 or table_number_booked <= 6 and table_number_booked not in small_tables_booked_list:
                    medium_tables_booked_list.append(table_number_booked) 
                    print("List medium tables booked", medium_tables_booked_list)

        if table_number in medium_tables_booked_list and len(medium_tables_booked_list) < 2:
            print("Table number" ,table_number,  "already booked")
            continue 

        elif len(medium_tables_booked_list) >= 2:
            print("tables length", len(medium_tables_booked_list))
            print("tables booked", medium_tables_booked_list)
            print("FULLY BOOKED")
            return False

        elif table_number not in medium_tables_booked_list:
           new_table = TableLunch.objects.create(table_id=booking_id,table_number=table_number,booked_for=people, table_max_people=table_max_people,table_status='confirmed',customer_name=customer_name,date=date,start_time=start_time )
           medium_tables_booked_list.append(table_number)
           print("Table number" ,table_number, " now booked")
           print("tables length", len(medium_tables_booked_list))
           print("print tables in list", medium_tables_booked_list)

           print("tables booked", medium_tables_booked_list)
           return True


def check_large_tables_available(people_requested, booking_id, customer_name, date, people, start_time):
    large_tables_booked_list = []

    while True:
        random_table_object = random.choice(Restaurant.large_table)
        table_number= random_table_object.get('table')
        table_max_people= random_table_object.get('max_px')

        tables_booked_requested_date = TableLunch.objects.filter(date=date).all()
        for table in tables_booked_requested_date.values():
            table = table.get('table_number')
            booked_tables_start_time_str = table.get('start_time').strftime("%H:%M")
            format_data = "%H:%M"
            booked_tables_start_time_str = booked_tables_start_time_str 
            service_finishing_time = "14:30"
            print("Print one table number for every loop and push it into tables booked", table_number_booked, "table start time", table.get('start_time') ) 
            if booked_tables_start_time_str <= service_finishing_time:
                if table_number_booked >= 7 or table_number_booked <= 8 and table_number_booked not in large_tables_booked_list:
                    small_tables_booked_list.append(table_number_booked) 
                    print("List large tables booked", large_tables_booked_list)
              

        if table_number in large_tables_booked_list and len(large_tables_booked_list) < 2:
            print("Table number" ,table_number,  "already booked")
            continue 

        elif len(large_tables_booked_list) >= 2:
            print("tables length", len(large_tables_booked_list))
            print("tables booked", large_tables_booked_list)
            print("FULLY BOOKED")
            return False

        elif table_number not in large_tables_booked_list:
           new_table = TableLunch.objects.create(table_id=booking_id,table_number=table_number,booked_for=people, table_max_people=table_max_people,table_status='confirmed',customer_name=customer_name,date=date,start_time=start_time )
           large_tables_booked_list.append(table_number)
           print("Table number" ,table_number, " now booked")
           print("tables length", len(large_tables_booked_list))
           print("print tables in list", large_tables_booked_list)

           print("tables booked", large_tables_booked_list)
           return True
        #    break




