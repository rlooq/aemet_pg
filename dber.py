'''Module to fetch data from JSON file, plot them and save them to a sqlite3 database'''

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def read_json(json_file):
    """Reads a given JSON file and returns a dataframe"""
    print("Reading JSON file: {}".format(json_file))
    jsondata=pd.read_json(json_file)
    print(jsondata.head())
    return jsondata

def plot_json(df):
    times=[i.split("T")[1][:-6] for i in df.fint]
    plt.plot(times, df["ta"], color="orange", label="Highs")
    plt.plot(times, df["vv"], color="blue", label="Wind Speed")
    plt.legend()
    plt.xlabel("Last 24h")
    plt.ylabel("Temperature (ºC) and Wind Speed (km/h)")
    plt.title("Temperatures and Wind Speed in C. UNIVERSITARIA - {}".format(df.iloc[-1, 3]))
    plt.grid(True)
    plt.show()

# Just creats DB, need to figure out how to update it with new data
def create_db(df):
    conn=sqlite3.connect("aemet.db")
    df.to_sql("cuniv", conn)
    conn.close()


if __name__ == "__main__":
    j=read_json("data_aemet_20190420-102259.json")
    #create_db(j)
    plot_json(j)
    