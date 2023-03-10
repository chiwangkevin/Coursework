from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Uses geo.rivers_with_station to print how many rivers have at least one monitoring station 
    (Representative result: 843) and prints the first 10 of these rivers in alphabetical order. Representative output:"""

    # Build list of stations
    stations = build_station_list()
    rivers_with_station_list = rivers_with_station(stations)
    print(str(len(rivers_with_station_list))+" rivers with station(s). The first 10 are...")
    print(sorted(rivers_with_station_list)[:10])
    '''
    Since a dictionary containing list of names of stations directing to their river nearby is created,
    the following codes refers to the names of stations by three rivers respectively, the order of appearance is ordered.
    '''
    stations_by_river_list = stations_by_river(stations)
    aire_stations = [i.name for i in stations_by_river_list["River Aire"]]
    cam_stations = [i.name for i in stations_by_river_list["River Cam"]]
    thames_stations = [i.name for i in stations_by_river_list["River Thames"]]
    print("River Aire")
    print(sorted(aire_stations))
    print("River Cam")
    print(sorted(cam_stations))
    print("River Thames")
    print(sorted(thames_stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
