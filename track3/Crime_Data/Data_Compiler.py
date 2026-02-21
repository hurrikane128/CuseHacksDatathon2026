import csv

import pandas as pd

data_files = ["Crime_Data_2023-1.csv", "Crime_Data_2023-2.csv", "Crime_Data_2024-1.csv", "Crime_Data_2024-2.csv"]

crime_dict = []

for item in data_files:
    with open(item) as cur_file:
        info = csv.reader(cur_file)
        for row in info:
            crime_dict.append({(row[0], row[1]): row[8]})

for index, item in enumerate(crime_dict):
    print(crime_dict[index])

