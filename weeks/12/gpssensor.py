# Virtual GPS sensor
# Generating GPSPoint(s)

from gpspoint import GPSPoint
import random


class GPSSensor:

    def __init__(self, pid : int = 1):
        self.pid = pid

    def read(self) -> GPSPoint:
        long = 5.0 + random.random() * 6.0
        lat = 60.0 + random.random() * 10.0
        height = -10.0 + random.random() * 2010
        point = GPSPoint(self.pid, long, lat, height)
        self.pid += 1
        return point
