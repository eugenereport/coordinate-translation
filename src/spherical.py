import math

class Spherical:
    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi

    @staticmethod
    def from_cartesian(x, y, z):
        r = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan2(y, x)
        phi = math.acos(z / r)
        return Spherical(r, theta, phi)

    def distance_through_volume(self, other_point):
        return math.sqrt(
            self.r**2 + other_point.r**2 - 2 * self.r * other_point.r *
            (math.sin(self.phi) * math.sin(other_point.phi) * math.cos(self.theta - other_point.theta) +
             math.cos(self.phi) * math.cos(other_point.phi))
        )

    def distance_on_surface(self, other_point):
        avg_r = (self.r + other_point.r) / 2
        
        return avg_r * math.acos(
            math.sin(self.phi) * math.sin(other_point.phi) +
            math.cos(self.phi) * math.cos(other_point.phi) * math.cos(self.theta - other_point.theta)
        )
