import math
from cartesian2d import Cartesian2D

class Polar:
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

    def distance(self, other_point):
        return math.sqrt(self.r ** 2 + other_point.r ** 2 - 2 * self.r * other_point.r * math.cos(self.theta - other_point.theta))

    @staticmethod
    def from_cartesian(x, y):
        r = math.sqrt(x * x + y * y)
        theta = math.atan2(y, x)

        if theta < 0:
            theta += 2 * math.pi

        return Polar(r, theta)
