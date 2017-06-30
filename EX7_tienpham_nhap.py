"""
Tien Pham
Metropolia University of Applied Sciences
Assignment 7: Internet
14/4/2017
How was the weather when you were born? 
"""


wu_api = "53697d26d3b6ed78"

url = "http://api.wunderground.com/api/53697d26d3b6ed78/history_19960809/q/vietnam/saigon.json"


import requests
def my_function(gooddate):
    urlstart = 'http://api.wunderground.com/api/INSERT_KEY_HERE/history_'
    urlend = '/q/vietnam/saigon.json'

    url = urlstart + str(gooddate) + urlend
    data = requests.get(url).json()
    for summary in data['history']['dailysummary']:
        print(','.join((gooddate,summary['date']['year'],summary['date']['mon'],summary['date']['mday'],summary['precipm'], summary['maxtempm'], summary['meantempm'],summary['mintempm'])))

       
        
my_function("19960809")                
                    
                    
    
	
