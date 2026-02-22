from BuildCrimeMap import createCrimeMap
from GenerateHeatMap import generateHeatMap

def crime_collector_main():
    crime_map = createCrimeMap()
    generateHeatMap(crime_map)

crime_collector_main()