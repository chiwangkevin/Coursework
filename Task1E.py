"""
Created Feb 2023
@author: at2017
In geo, a function that determines the N rivers with the greatest number of monitoring stations is created,
It should return a list of (river name, number of stations) tuples
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E, It should return a list of (river name, number of stations) tuples
    It should print the top nine(in the number of stations) river with their number of stations."""
    stations = build_station_list()
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
