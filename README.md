# aemet_pg
Playing with the [AEMET API](https://opendata.aemet.es/centrodedescargas/inicio) and [AQICN.org](https://aqicn.org/api/) to collect weather and air quality data.

 - `aemet.py` requests info form AEMET, using functions from `dber.py`, and does the following (for Ciudad Universitaria Weather Station in Madrid):
	1. Prints hourly highs and lows in the last 24 hours
	2. Prints extreme values (highes and lowest temperatures)
	3. Saves data in json as: data_aemet_[date_and_time].json
	4. Saves a graphic for temperature and wind as graph_[date_and_time].png
	5. Creates or updates a SQLite database called `aemet.db`

 - `aemet_csv.py` just downloads a CSV file with weather observation info from one specific station: Ciudad Universitaria, in Madrid.

 - `air_quality.py` prints air quality information from http://api.waqi.info for a given city.

 - `air_quality_func.py` does the same, but uses functions and downloads a JSON file and a text file with more complete information.

 - `airq_pdf.py` just downloads a pdf with the current air quality information from the city council in Madrid (munimadrid.es).