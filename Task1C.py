from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C: to build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). 
    Print the names of the stations, listed in alphabetical order.
    """

    # Build list of stations, the 10th line is to filter the stations that is within the range 10km.
    stations = build_station_list()
    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    alphabetically_sorted = sorted(stations_within_radius_list, key=lambda x: x.name)
    #i.name means the the name of a certain object
    print([i.name for i in alphabetically_sorted])

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
