#lat for 2023
import csv
column_index = 9
with open("Crime_Data/Crime_Data_2023-1.csv", "r") as f:
    reader = csv.reader(f)
    column = [row[column_index] for row in reader]
print(column)

### csv parse -> row
### row -> x,y for the 2D list (from long and lat), type of crime, and

# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

# { "LARCENY":1, ... }