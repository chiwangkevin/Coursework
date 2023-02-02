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
