"""Downloads aemet CSV with weather observation from one specific station: Ciudad Universitaria"""

import sys
import requests as req
import time

hoy=time.strftime("%Y%m%d-%H%M%S")

url = "http://www.aemet.es/es/eltiempo/observacion/ultimosdatos_3194U_datos-horarios.csv?k=mad&l=3194U&datos=det&w=0&f=temperatura&x=h24"
response = req.get(url)

with open(r"c:\pg\aemet\aemet_observacion_{}.csv".format(hoy), "w") as f:
        f.write(response.text)

print("Data saved to CSV file.")