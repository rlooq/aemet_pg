'''Functions to fetch data from JSON file, plot them and save them to a sqlite3 database'''

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


def read_json(json_file):
    """Reads a given JSON file and returns a simplified dataframe"""
    print("Reading JSON file: {}".format(json_file))
    jsondata=pd.read_json(json_file)
    jsondata=jsondata[["fint", "hr", "prec", "rviento", "ta", "tamax", "tamin", "vmax", "vv"]]
    print(jsondata.head())
    return jsondata


def plot_json(df):
    datadate=df.iloc[-1,0][:-6].replace("T", " at ")
    times=[i.split("T")[1][:-6] for i in df.fint]
    plt.plot(times, df["ta"], color="orange", label="Temperatures")
    plt.plot(times, df["vv"], color="blue", label="Wind Speed")
    plt.legend()
    plt.xlabel("Last 24h")
    plt.ylabel("Temperature (ºC) and Wind Speed (km/h)")
    plt.title("Temperature and Wind Speed in C. UNIVERSITARIA - {}h".format(datadate))
    plt.grid(True)
    #plt.show()
    plt.savefig("graph_{}.png".format(datadate))


def create_db(df):
    conn=sqlite3.connect("aemet.db")
    df.to_sql("cuniv", conn)
    conn.close()


def update_db(df):
    conn=sqlite3.connect("aemet.db")
    df.to_sql("cuniv", conn, if_exists="append", index=False)
    conn.close()


""" def remove_duplicates():
    conn = sqlite3.connect("aemet.db")
    with conn:    
        cur = conn.cursor()    
        cur.execute("SELECT fint, COUNT(*) FROM cuniv GROUP BY fint HAVING COUNT(*) > 1")
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print("Duplicate: {}".format(row)) """



if __name__ == "__main__":
    j=read_json("data_aemet_20190420-102259.json")
    plot_json(j)
    