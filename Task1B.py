from floodsystem.stationdata import build_station_list
from floodsystem.geo import station_by_distance

def run():
    """Requirements for Task 1B: to define the function that is responsible for filter the 10 closest and the 10 furthest stations from the Cambridge city centre"""

    # Build list of stations
    stations = build_station_list()
    #Example Code
    station_by_distance_list = station_by_distance(stations, (52.2053,0.1218))
    nearest_10=[]
    print("Nearest")
    '''   
    Add sorted turple result from the tenth nearest list (name of the twown, distance)
    '''
    for i in station_by_distance_list[:10]:
        nearest_10.append((i[0].name, i[1]))
    print(nearest_10)
    
    print("Furthest")
    '''   
    Add sorted turple result from the tenth furthest list (name of the town, distance)
    '''
    furthest_10=[]
    for i in station_by_distance_list[-10:]:
        furthest_10.append((i[0].name, i[1]))
    print(furthest_10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
