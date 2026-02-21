#lat for 2023
import csv
column_index_lat = 10
with open("Crime_Data/Crime_Data_2023-1.csv", "r") as f:
    reader = csv.reader(f)
    column = [row[column_index_lat] for row in reader]
latitudes20231 = column
print(column)