"""Gets air cuality based on entered location"""

import sys
import time
import json
import requests as req

# Getting key from a different file
import credentials
token = credentials.key_waqi

city=input("Enter the name of the city... ")

# Requesting information
url = "http://api.waqi.info/feed/{}/?token={}".format(city, token)
response = req.get(url, verify=False)
if response.json()['status'] == "ok":
    print("The air quality is {}".format(response.json()['data']['aqi']))
    
    print("Other values are:\n")
    for k, v in response.json()['data']['iaqi'].items():
        for i in v.values(): 
            print(" {}\t{}".format(k, i))
    
    print("The data was fetched from " +
    response.json()['data']['city']['name'])
    print("The pollutant measured was " + str(response.json()['data']['dominentpol']))
    
    # Saving json file with a date/time stamp of today.
    hoy=time.strftime("%Y%m%d-%H%M%S")
    with open("data_waqi_{}.json".format(hoy), "w") as outfile:
        json.dump(response.json(), outfile)

    # Saving a more readable text file.
    
    with open("data_waqi_{}.txt".format(hoy), "w") as textfile:
        for k, v in response.json()["data"]["city"].items():
            textfile.write("{}: {}\n".format(k, v))
        for k, v in response.json()["data"]["iaqi"].items():
            for i in v.values():
                textfile.write("{}: {}\n".format(k, i))
        textfile.write("Time: {}".format(response.json()["data"]["time"]["s"]))

elif response.json()['status'] == "error":
    print("The server returned an error. The message is " + response.json()['data'])
else:
    print("Cannot fetch AQI without token")