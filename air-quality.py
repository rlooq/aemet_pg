"""Gets air cuality based on entered location"""

import sys
import time
import json
import requests as req

# Getting key from a different file
import credentials
token = credentials.key_waqi

city=input("Enter the name of the city... ")

url = "http://api.waqi.info/feed/{}/?token={}".format(city, token)
response = req.get(url, verify=False)
if response.json()['status'] == "ok":
    print("The air quality is " + str(response.json()['data']['aqi']))
    
    print("Other values are:\n")
    for k, v in response.json()['data']['iaqi'].items():
        for i in v.values(): 
            print(k, "\t", str(i))
    
    print("The data was fetched from " +
    response.json()['data']['city']['name'])
    print("The pollutant measured was " + str(response.json()['data']['dominentpol']))
    
    # Saving json file with a date/time stamp of today.
    hoy=time.strftime("%Y%m%d-%H%M%S")
    with open("data_waqi_{}.json".format(hoy), "w") as outfile:
        json.dump(response.json(), outfile)
elif response.json()['status'] == "error":
    print("The server returned an error. The message is " + response.json()['data'])
else:
    print("Cannot fetch AQI without token")
