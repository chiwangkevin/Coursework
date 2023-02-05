from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
def run():
  stations=build_station_list()
  position_of_cam=(52.2053, 0.1218)
  output = stations_by_distance(stations, p_cam_center)
   # change each element from (obj, dis) to (name, town, dis)
    output = [(station.name, station.town, distance) for station, distance in output]
  
  
    print(output[:10])
    print()
    print(output[-10:])
    return [output[:10], output[-10:]]
if __name__ == "__main__":
    run()
