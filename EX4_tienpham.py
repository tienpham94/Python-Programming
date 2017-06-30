"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 4: Branches
14/4/2017
"""

import datetime
from time import gmtime,strftime

def my_function(name,age):
    favorite_colour = input("What is your farorite color? ")
    my_tuple=("Hi, my name is ",", I'm "," years old, and I like " , ". Today is ",". My "," number is ", ": going to sleep now!")
    this_date = strftime("%d-%m-%y", gmtime())
    day = datetime.datetime.today().day
    hour = datetime.datetime.today().hour
    minute = datetime.datetime.today().minute

    if hour >= 22:
        go_to_sleep = "".join([str(hour) + ":" + str(minute) + my_tuple[6]])
        return go_to_sleep

    try: 
        lucky_number = (int(age) - int(day))%int(hour)
    except ZeroDivisionError:
        lucky_number = 0

    special = ""    
    if lucky_number == 0 :
        special = "funny"
    elif lucky_number in range(1,3) :
        special = "normal"
    elif lucky_number in range(4,7) :
        special = "sunny"
    else :
        special = "great"

    my_string = "".join([my_tuple[0],str(name), my_tuple[1],str(age),my_tuple[2], str(favorite_colour), my_tuple[3],str(this_date), my_tuple[4],special, my_tuple[5], str(lucky_number), "."])
    return my_string

print(my_function("tien",22))
    
