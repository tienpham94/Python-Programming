"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 7: Internet
14/4/2017
How was the weather when you were born? 
"""

import urllib.request
import json

wu_api = "53697d26d3b6ed78"
my_birthday = 19970622

def my_weather(day,api):
    url = "http://api.wunderground.com/api/"+ str(api) +"/history_" + str(day) + "/q/vietnam/saigon.json"
    response = urllib.request.urlopen(url).read()
    json_obj = str(response,"utf-8")
    data = json.loads(json_obj)

    #tuple to store string sentences
    info =("I was born at ", " in ", "The weather at that time was ","The temperature was "," °C")
    
    print("".join([info[0],data["history"]["observations"][5]["date"]["pretty"],info[1],data["history"]["date"]["tzname"]]))
    print("".join([info[2],data["history"]["observations"][5]["conds"]]))
    print("".join([info[3],data["history"]["observations"][5]["tempm"],info[4]]))
       
my_weather(my_birthday,wu_api)                    
                    
    
	
