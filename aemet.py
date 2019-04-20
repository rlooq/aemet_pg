'''A script to download weather data for the last 24 hour from the C. Univ station.
   The data are saved to a json file and the temperature/wind speed are plotted.'''

import requests
from requests.exceptions import HTTPError
import json
import time

# Login information from external file
import credentials
from dber import *

# Request information
url = "https://opendata.aemet.es/opendata/api/observacion/convencional/datos/estacion/3194U"
headers = {"cache-control": "no-cache"}
querystring = credentials.key_aemet

try:
	response = requests.get(url, headers=headers, params=querystring)
	response.raise_for_status()

	print("This is the response text, which only has metadata, so we'll use the returned URL from 'datos':\n{}".format(response.text))

	address=response.json()['datos']

	# Requesting that json url, which will return a json object with 24h worth of datapoints
	req=requests.get(address, headers)

	# Saving json file with a date/time stamp of today.
	hoy=time.strftime("%Y%m%d-%H%M%S")
	json_filename="data_aemet_{}.json".format(hoy)
	with open(json_filename, "w") as f:
		json.dump(req.json(), f)
	print('\nData downloaded from {}\nSaved into file as {}.\n'.format(req.url, json_filename))

	# Printing results
	print("\nThe max/min temperatures from C. Univ for the last 24h have been these:\n")

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
	
	# Read and plot the JSON file
	plot_json(read_json("data_aemet_{}.json".format(hoy)))

except HTTPError as http_err:
    print('HTTP error occurred: {}'.format(http_err))
except Exception as err:
    print('Other error occurred: {}'.format(err))
else:
        print('\nEverything went well!')


# TO-DOs: Create a DB to populate regularly with the data gathered here,
# so as to use it later to generate graphics and statistics.