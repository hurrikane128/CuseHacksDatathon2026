#lat for 2023
import csv
from scale_0_to_24 import latlon_to_grid
import parameters as params

crime_map = []
# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

grid_size = params.CRIME_MAP_WIDTH

for y in range(0, grid_size):
    temp_list = []
    for x in range(0, grid_size):
        temp_list.append({"LARCENY":0, "MV THEFT":0})
    crime_map.append(temp_list)

data_files = ["Crime_Data_2023-1.csv", "Crime_Data_2023-2.csv", "Crime_Data_2024-1.csv", "Crime_Data_2024-2.csv"]

for i in range(4):
    item = data_files[i]
    with open('Crime_Data/'+item) as cur_file:
        t = cur_file.readline()
        info = csv.reader(cur_file)
        for row in info:
            num = 0
            if not (row[6] == "False" or row[6] == "True"):
                num = 1

            ## Finding x and y and crime type
            lat = row[9 + num]
            long = row[10 + num]
            y, x = latlon_to_grid(float(lat), float(long), params.MinLat[i], params.MaxLat[i], params.MinLong[i], params.MaxLong[i], grid_size)
            #x = convertLong(long)
            #y = convertLat(lat)
            crime_type = row[7 + num] # 7 - crime type

            ## Adding the crime to the crime map
            if crime_type in crime_map[y][x].keys():
                crime_map[y][x][crime_type] += 1  # 7 - crime
            else:
                crime_map[y][x][crime_type] = 1

print(crime_map)
### csv parse -> row
### row -> x,y for the 2D list (from long and lat), type of crime, and

# [
#   [{}, {}, {}],
#   [{}, {}, {}],
#   [{}, {}, {}],
# ]

# { "LARCENY":1, ... }