"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 2: Variables
14/4/2017
"""

import datetime
from time import gmtime,strftime

name = input("What is your name? ")
age = input("What is your age? ")
favorite_colour = input("What is your farorite color? ")

my_tuple=("Hi, my name is ",", I'm "," years old, and I like " , ". Today is ",". My lucky number is ")
this_date = strftime("%d-%m-%y", gmtime())
day = datetime.datetime.today().day
hour = datetime.datetime.today().hour

#try except if hour == 0
try: 
    lucky_number = (int(age) - int(day))%int(hour)
except ZeroDivisionError:
    lucky_number = 0

my_string = "".join([my_tuple[0],str(name), my_tuple[1],str(age),my_tuple[2], str(favorite_colour), my_tuple[3],str(this_date), my_tuple[4], str(lucky_number), "."])
print(my_string)
