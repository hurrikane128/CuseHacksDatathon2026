#lat for 2023
import csv
with open("Crime_Data/Crime_Data_2023-1.csv", "r") as f:
    test = f.readline()
    reader = csv.reader(f)
    list12023 = []
    for row in reader:
        #print(row)
        lat = row[9]
        long = row[10]
        list12023.append(lat)
        list12023.append(long)

with open("Crime_Data/Crime_Data_2023-2.csv", "r") as f:
    test = f.readline()
    reader = csv.reader(f)
    list22023 = []
    for row in reader:
        #print(row)
        lat = row[9]
        long = row[10]
        list22023.append(lat)
        list22023.append(long)

with open("Crime_Data/Crime_Data_2024-1.csv", "r") as f:
    test = f.readline()
    reader = csv.reader(f)
    list12024 = []
    for row in reader:
        #print(row)
        lat = row[9]
        long = row[10]
        list12024.append(lat)
        list12024.append(long)

with open("Crime_Data/Crime_Data_2024-2.csv", "r") as f:
    test = f.readline()
    reader = csv.reader(f)
    list22024 = []
    for row in reader:
        #print(row)
        lat = row[8]
        long = row[9]
        list22024.append(lat)
        list22024.append(long)
print(list12023)
print("\n")
print(list22023)
print("\n")
print(list12024)
print("\n")
print(list22024)

### csv parse -> row
### row -> x,y for the 2D list (from long and lat), type of crime, and

# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

# { "LARCENY":1, ... }