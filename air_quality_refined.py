import time
import json
import requests as req

# Getting key from a different file
import credentials
token = credentials.key_waqi

now=time.strftime("%Y%m%d_%H%M%S")


def data_fetch(city):
    """Fetches data from WAQI API for a given city and returns JSON"""
    url = "http://api.waqi.info/feed/{}/?token={}".format(city, token)
    response = req.get(url, verify=False)
    if response.json()['status'] == "ok":
        print("\nThe air quality is {}\n".format(response.json()['data']['aqi']))
        return response.json()
    
    elif response.json()['status'] == "error":
        print("The server returned an error. The message is " + response.json()['data'])
    else:
        print("Cannot fetch AQI without token")


def save_json(j):
    """Saves a given JSON file resulting from data_fetch()"""
    with open("data_waqi_{}.json".format(now), "w") as outfile:
        json.dump(j, outfile)
    print("JSON file saved as: data_waqi_{}.json\n".format(now))


def data_extract(j):
    """Extracts relevant info from JSON file resulting from data_fetch() """
    data_lines=[]
    data_lines.append("Data for {}".format(j['data']['city']['name']))
    for k, v in j['data']['iaqi'].items():
        for i in v.values(): 
            data_lines.append("{}\t{}".format(k, i))
    data_lines.append("Time: {}".format(j["data"]["time"]["s"]))
    return data_lines


def save_text(info):
    """Saves relevant info (list of lines extracted with data_extract)"""
    with open("data_waqi_{}.txt".format(now), "w") as textfile:
        for line in info:
            textfile.write("{}\n".format(line))
    print("Text file saved as: data_waqi_{}.txt\n".format(now))

if __name__ == "__main__":
    jason=data_fetch("Madrid")
    save_json(jason)
    save_text(data_extract(jason))


