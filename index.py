import mysql.connector
from datetime import date
import random
import string

# """------------Asansol to Medinipur Booking-------------"""
def bus1(connection, cur):
   pname = input("Enter Your name :")
   pAge = int(input("Enter your age : "))
   pcon = int(input("Enter Conatact Number : "))
   date_components = input('Enter a date formatted as YYYY-MM-DD : ').split('-')
   year, month, day = [int(item) for item in date_components]
   JourneyDate = date(year , month , day)
   from_place = "Asansol";
   to_place = "Medinipur";
   ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

   query = "insert into BUS1(passenger_name ,passenger_age, contact, journey_date,from_place,to_place,ticket_number)"
