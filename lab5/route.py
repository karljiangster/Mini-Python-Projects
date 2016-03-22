import coordinates

class Route(object):
    def __init__(self):
<<<<<<< HEAD
        # replace pass with your code
        pass
    

    # Your methods here
=======
       
        self.coordinates = []
    

    # Your methods here
    def append_GPS_coordinates(gps_coordinate):
    	self.coordinates.append(gps_coordinate)

    def get_total_distance(self): 
    	total_distance = 0
    	for i, coordinates in enumerate(self.coordinates): 
    		total_distance += coordinates.distance_to(self.coordinates[i+1]) 

    	return total_distance

    def get_max_elevation_change(self): 
    	assert len(self.coordinates) > 1

    	max_elevation = self.coordinates[1].distance_to(self.coordinates[0])
    	for i, coordinate in enumerate(self.coordinates): 
    		if i + 1 == len(self.coordinates): 
    			break 
    		else: 
    			next = self.coordinates[i + 1]
    			current_elevation = next.distance_to(coordinate)
    			if current_elevation > max_elevation: 
    				max_elevation = current_elevation
    	return max_elevation
>>>>>>> ccf00b4aa296831ae57443e689cae1646443c138
