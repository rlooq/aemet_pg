'''A script to download weather data from the last 24 hour in the C. Univ station.
   The data are saved to a json file for now. Aiming at creating a DB at some point.'''

from requests.auth import HTTPBasicAuth
import requests
import json
import time

# Login information from external file
import credentials

url = "https://opendata.aemet.es/opendata/api/observacion/convencional/datos/estacion/3194U"
headers = {"cache-control": "no-cache"}
querystring = credentials.key_aemet

response = requests.get(url, headers=headers, params=querystring)

print("This is the response text, which only gives me headers, so I'll use the returned URL from 'datos':\n", response.text)

# The response only gives me headers, etc. and a json url that I can use
address=response.json()['datos']

# Requesting that json url, which will return a json object with 24h worth of datapoints
req=requests.get(address, headers)

# Saving json file with a date/time stamp of today.
hoy=time.strftime("%Y%m%d-%H%M%S")
with open("data_aemet_{}.json".format(hoy), "w") as outfile:
    json.dump(req.json(), outfile)

print("\nData downloaded from {}\nSaved into file as data.json.\n".format(req.url))

# Printing results
print("The max/min temperatures from C. Univ for the last 24h have been these:\n")

dicky={}
maxlist=[]
minlist=[]

for i in req.json():
	dicky[i["fint"]]=[i["tamax"], i["tamin"]]
	maxlist.append(i["tamax"])
	minlist.append(i["tamin"])
for k, v in dicky.items():
	print("Time: {}\tMax: {}\t Min: {}".format(str(k.split(sep="T")), v[0], v[1]))

print("\nExtremes for this period:\nHigh:\t {} degrees.\nLow:\t {} degrees.".format(max(maxlist), min(minlist)))


# To do: load the data from this json file and save it to a sqlite db, or an excel or csv
# so as to use it later to generate graphics and statistics