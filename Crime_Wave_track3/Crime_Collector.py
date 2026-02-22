from BuildCrimeMap import createCrimeMap
from GenerateHeatMap import generateHeatMap

def crime_collector_main():
    crime_map = createCrimeMap()
    print(crime_map)
    generateHeatMap(crime_map, 'OFFN AGAINST FAMILY')

crime_collector_main()