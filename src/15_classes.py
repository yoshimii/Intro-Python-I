# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        self.lat = lat
        self.lon = lon
        
    def print_waypoint(name, lat, lon ):
        print(name, lat, lon)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint, LatLon):
    def __init__(self, name, difficulty, size,  lat, lon):
        super().__init__(name, lat, lon)
        self.lat = lat
        self.lon = lon
        self.name = name
        self.difficulty = difficulty
        print(name, difficulty, size, lat, lon)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

Waypoint.print_waypoint("Catacombs", 41.70505, -121.51521)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

Geocache("Newberry Views", "dif 1.5", "size 2", 44.052137, -121.41556)


