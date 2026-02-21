#lat for 2023
import csv

CRIME_MAP_WIDTH = 25
CRIME_MAP_HEIGHT = 25

crime_map = []
# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

def convertLat( Lat ):
    return 0
def convertLong( Long ):
    return 0

for y in range(0, CRIME_MAP_HEIGHT):
    temp_list = []
    for x in range(0, CRIME_MAP_WIDTH):
        temp_list.append({"LARCENY":0, "MV THEFT":0})
    crime_map.append(temp_list)

print(crime_map)

data_files = ["Crime_Data_2023-1.csv", "Crime_Data_2023-2.csv", "Crime_Data_2024-1.csv", "Crime_Data_2024-2.csv"]

for item in data_files:
    with open('Crime_Data/'+item) as cur_file:
        t = cur_file.readline()
        info = csv.reader(cur_file)
        for row in info:
            i = 0
            if not (row[6] == "False" or row[6] == "True"):
                i = 1

            ## Finding x and y and crime type
            lat = row[9 + i]
            long = row[10 + i]
            x = convertLong(long)
            y = convertLat(lat)
            crime_type = row[7 + i] # 7 - crime type

            ## Adding the crime to the crime map
            if crime_type in crime_map[y][x].keys():
                crime_map[y][x][crime_type] += 1  # 7 - crime
            else:
                crime_map[y][x][crime_type] = 1
### csv parse -> row
### row -> x,y for the 2D list (from long and lat), type of crime, and

# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

# { "LARCENY":1, ... }