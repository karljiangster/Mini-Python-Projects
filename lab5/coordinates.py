import math

class Coordinates(object):
    EARTH_RADIUS = 6371000.0

    def __init__(self, latitude, longitude):
        # replace pass with your code
<<<<<<< HEAD
        pass

    def distance_to(self, other):
        # your code here
        # replace 0.0 with appropriate return value
        return 0.0
=======
        self.longitude = longitude
        self.latitude = latitude


    @property 
    def longitude(self): 
        return self._longitude 
    

    @longitude.setter 
    def longitude(self, longitude): 
        if not isinstance(longitude, (int, float)): raise ValueError("Not a number")
        self._longitude = longitude


    @property 
    def latitude(self): 
        return self._latitude 


    @latitude.setter
    def latitude(self, latitude): 
        if not isinstance(latitude, (int, float)): raise ValueError("Not a number")
        self._latitude = latitude


    def distance_to(self, other):
        # your code here

        if not isinstance(other, Coordinates): raise ValueError("Not a number")
        
        self_lat_rad = math.radians(self.latitude)
        self_lo_rad = math.radians(self.longitude)
        other_lat_rad = math.radians(other.latitude)
        other_lo_rad = math.radians(other.longitude)

        midpoint_lat = (self_lat_rad - other_lat_rad)/2 
        midpoint_lo = (self_lo_rad - other_lo_rad)/2

        first_term = math.sin(midpoint_lat)**2 
        cos_lat = math.cos(other_lat_rad) * math.cos(self_lat_rad)
        second_term = cos_lat * math.sin(midpoint_lo)**2 
        inside_arcsin = math.sqrt(first_term + second_term)

        distance = 2 * Coordinates.EARTH_RADIUS * math.asin(inside_arcsin)

        return distance 
>>>>>>> ccf00b4aa296831ae57443e689cae1646443c138


    def __str__(self):
        # your code here
        # replace "" with appropriate return value
<<<<<<< HEAD
        return ""
=======

        return "Latitude is " + str(self.latitude) + "\nLongitude is " + str(self.longitude)
>>>>>>> ccf00b4aa296831ae57443e689cae1646443c138

