from pygame.math import Vector2
from pygame.rect import Rect
import random


def random_color() -> (int, int, int):
    return random.randint(30, 250), random.randint(30, 250), random.randint(30, 250)


class Body:

    def __init__(
            self,
            mass: int,
            coordinates: Rect,
            velocity: Vector2,
            game_instance,
            color: (int, int, int) = None
    ):
        self.mass = mass
        self.coordinates = coordinates
        self.x = float(coordinates.x)
        self.y = float(coordinates.y)
        self.velocity = velocity
        from game import Game
        self.game: Game = game_instance
        if not color:
            self.color = random_color()
        else:
            self.color = color
