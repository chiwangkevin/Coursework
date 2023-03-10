# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data
"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town): #Define all relevant attributes

        """
        The method __init__ initialises a station with data
        """
        
        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        
        """
        The method __repr__ prints a description of the station
        """
        
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):

        '''Takes in self (station object)
        Returns True when typical range is in a correct order
        Returns False when typical range is in a wrong order/does not exist
        '''

        if self.typical_range == None:
            return False
        elif self.typical_range[0] <= self.typical_range[1]:
            return True
        else:
            return False

    def relative_water_level(self):

        '''Takes in self (station object)
        Returns a value from 0.0 to 1.0 describing the latest relative water level
        Returns None when data is out of range or inconsistent
        '''

        if (not self.typical_range_consistent()) or (self.latest_level==None):
            return None
        return (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])


def inconsistent_typical_range_stations(stations):

    '''Takes in a list of station objects
    Returns a list of station objects with inconsistent typical range
    '''

    inconsistent_list = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_list.append(station)
    return inconsistent_list
