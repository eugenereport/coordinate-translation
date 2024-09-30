import math

class Cartesian2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    @staticmethod
    def from_polar(r, theta):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return Cartesian2D(x, y)
