# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.haversine import haversine as hs
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
  
    output = []

    # collect all the (station, distance)
    for i in stations:
        distance = hs(i.coord, p)
        output.append((station, distance))

    # sort the output tuples with respect to distance
    output = sorted_by_key(output, 1)

    return output
  
def stations_within_radius(stations, center, r):
    
    new_stations = []
    for i in stations:
        distance = hs(i.coord, center)
        if distance < r:
            new_stations.append(station)
            
    return new_stations
  
 def rivers_with_stations(stations):
    '''
    This function returns a set of the name of rivers having at least one station
    Input :
        stations:      a list of MonitoringStation objects
    '''
    #get the name of rivers with stations
    rivers = set()
    for station in stations:
        rivers.add(station.river)
        
    return rivers
        
def stations_by_river(stations):
    '''
    This function returns a dictionary that map river names to a list of station objects on the river.
    Input :
        stations:      a list of MonitoringStation objects
    '''
    
    rivers_with_st = dict()
    
    for river in rivers_with_stations(stations):
        list_of_st = []
        
        for station in stations:
            #forming a list with stations of that river
            if station.river == river:
                list_of_st.append(station.name)
        #adding the list into map
        rivers_with_st[river] = list_of_st
        
    return rivers_with_st
