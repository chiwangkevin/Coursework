from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def run():   
    stations = build_station_list()
    center_cam = (52.2053, 0.1218)
    r_cam = 10
    list_stations_within_range = stations_within_radius(stations, center_cam, r_cam)
    
    #generate the list of stations within the distance
    name_list = []
    for st in list_stations_within_range :
        name_list.append(st.name)
    
    #sorted the list by alphabetic order
    sorted_list = sorted(name_list)
    print(sorted_list)
    return sorted_list
    
if __name__ == "__main__":
    run()
