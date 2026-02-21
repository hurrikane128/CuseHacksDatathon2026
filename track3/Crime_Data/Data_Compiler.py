import pandas as pd

data_files = ["Crime_Data_2024-1.csv", "Crime_Data_2024-2.csv"]


crime_dict = {}

for item in data_files:
    with open(item, "r") as cur_file:
        info = cur_file.readlines()
        print(info)


