#lat for 2023
import csv
column_index = 10
with open("Crime_Data_2023-1.csv", "r") as f:
    reader = csv.reader(f)
    column = [row[column_index] for row in reader]
print(column)
