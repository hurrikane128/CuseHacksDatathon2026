from BuildCrimeMap import createCrimeMap
from GenerateHeatMap import generateHeatMap

def crime_collector_main():
    flag_year = False # if true, it will collect only 2023 or 2024,
                     # otherwise both years
    year = '2024'    # if not 2023, will collect data from 2024,
                     # otherwise from 2023

    crime_map = createCrimeMap(flag_year, year)
    print(crime_map)
    generateHeatMap(crime_map, '', flag_year, year) # for 2nd parameter, you can input a specific crime type from CRIME_TYPES

crime_collector_main()