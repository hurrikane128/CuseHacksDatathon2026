#lat for 2023
import csv
column_index = 9
with open("Crime_Data/Crime_Data_2023-1.csv", "r") as f:
    test = f.readline()
    reader = csv.reader(f)
    list12023 = []
    for row in reader:
        #print(row)
        lat = row[9]
        long = row[10]
        list12023.append(lat + " " + long)
print(list12023)

### csv parse -> row
### row -> x,y for the 2D list (from long and lat), type of crime, and

# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

# { "LARCENY":1, ... }