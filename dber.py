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
    plt.plot(times, df["tamax"], color="orange", label="Highs")
    plt.plot(times, df["tamin"], color="blue", label="Lows")
    plt.legend()
    plt.xlabel("Last 24h")
    plt.ylabel("Temperatures")
    plt.title("Temperatures in C. Universitaria - {}".format(df.fint[23]))
    plt.grid(True)
    plt.show()


def create_db(df):
    conn=sqlite3.connect("aemet.db")
    df.to_sql("cuniv", conn)
    conn.close()


if __name__ == "__main__":
    j=read_json("data_aemet_20190419-152858.json")
    #create_db(j)
    plot_json(j)
    