import math

class Cartesian3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2 +
            (self.z - other_point.z) ** 2
        )

    @staticmethod
    def from_spherical(r, theta, phi):
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        return Cartesian3D(x, y, z)
