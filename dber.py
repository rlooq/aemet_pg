'''Module to fetch data from JSON file, plot them and save them to a sqlite3 database'''

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def read_json(json_file):
    print("Reading JSON file: {}".format(json_file))
    jsondata=pd.read_json(json_file)
    print(jsondata.head())
    return jsondata

# Need to find out how to plot with matplotlib
def plot_json(df):
    pass


def create_db(df):
    conn=sqlite3.connect("aemet.db")
    df.to_sql("cuniv", conn)
    conn.close()


if __name__ == "__main__":
    create_db(read_json(""))
    