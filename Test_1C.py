from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    '''
    Test for stations_within_radius
    '''
    # generate stations list
    stations = build_station_list()
    
    #get the distance
    center_cam = (52.2053, 0.1218)
    r_cam = 10
    list_st_within = stations_within_radius(stations, center_cam, r_cam)
    
    #generate the list of stations within the distance
    name_list = []
    for st in list_st_within:
        name_list.append(st.name)
    
    #sorted the list by alphabetic order
    sorted_list = sorted(name_list)
    print(sorted_list)
    return sorted_list
    
if __name__ == "__main__":
    run()
