from math import radians, cos, sin, asin, sqrt
EARTH_RADIUS = 6371  # in km
MILES_PER_KM = 0.621371

def haversine(point1, point2, miles=False):
    """ Calculate distance in 3-D space. Miles can be returned
    if the ``miles`` parameter is set to True.
    """
    # unpack latitude/longitude
    (lat1, lng1) = point1
    (lat2, lng2) = point2

    #convert to radian
    lat11=radians(lat1)
    lng11=radians(lng1)
    lat22=radians(lat2)
    lng22=radians(lat2)
    # calculate haversine
    lat = lat22 - lat11
    lng = lng22 - lng11
    d = sin(lat * 0.5) ** 2 + cos(lat11) * cos(lat22) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * MILES_PER_KILOMETER # in miles
    else:
        return h  # in kilometers
