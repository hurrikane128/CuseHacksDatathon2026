import csv

import pandas as pd

data_files = ["Crime_Data_2024-1.csv"]

crime_dict = {}

for item in data_files:
    with open(item) as cur_file:
        info = csv.reader(cur_file)
        for row in info:
            print("X: " + str(row[0]), "Y: " + str(row[1]), "Crime: " + str(row[8]))


