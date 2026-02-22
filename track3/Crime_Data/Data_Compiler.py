import csv

#import pandas as pd

data_files = ["Crime_Data_2023-1.csv", "Crime_Data_2023-2.csv", "Crime_Data_2024-1.csv", "Crime_Data_2024-2.csv"]

crime_list = []


def read_files():
    for item in data_files:
        with open(item) as cur_file:
            info = csv.reader(cur_file)
            for row in info:
                if row[6] == "False" or row[6] == "True":
                    try:
                        crime_list.append([float(row[8]), float(row[9]), row[7]])
                    except ValueError:
                        pass
                else:
                    try:
                        crime_list.append([float(row[9]), float(row[10]), row[8]])
                    except ValueError:
                        pass
    '''
    for index, item in enumerate(crime_list):
        print(index)
        print(item)
    '''
    return crime_list

#read_files()



