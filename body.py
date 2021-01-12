from pygame.math import Vector2
from pygame.rect import Rect


class Body:

    def __init__(self, mass: int, semi_minor_axis: float, coordinates: Rect, velocity: Vector2):
        self.mass = mass
        self.semi_minor_axis = semi_minor_axis
        self.coordinates = coordinates
        self.x = float(coordinates.x)
        self.y = float(coordinates.y)
        self.velocity = velocity
