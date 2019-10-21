"""Downloads boletin diario of Madrid pollution in PDF format"""

import sys
import requests as req
import datetime

hoy=datetime.datetime.today().__str__()[:10]

# This pdf is published every Wednesday
url = "http://www.mambiente.munimadrid.es/datos_prevalidados/boletin_diario.pdf"
response = req.get(url)

with open(r"c:\pg\aemet_pg\boletin_pollution_{}.pdf".format(hoy), "wb") as f:
        f.write(response.content)

