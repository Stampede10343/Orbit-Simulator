import math

from pygame.math import Vector2
from pygame.rect import Rect
import random

import game

from pygame import gfxdraw


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, int(radius), color)
    gfxdraw.filled_circle(surface, x, y, int(radius), color)


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
        self.__coordinates = coordinates
        self.__x = float(coordinates.x * game_instance.scale)
        self.__y = float(coordinates.y * game_instance.scale)
        self.velocity = velocity
        from game import Game
        self.game: Game = game_instance
        if not color:
            self.color = random_color()
        else:
            self.color = color

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
        self.coordinates.x = x / self.game.scale

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
        self.coordinates.y = y / self.game.scale

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    def draw(self):
        if self.x >= 30000 or self.y >= 30000 or self.x <= -30000 or self.y <= -30000:
            self.game.planets.remove(self)
            return

        draw_circle(self.game.screen,
                    self.coordinates.x,
                    self.coordinates.y,
                    self.mass ** (1 / 8),
                    self.color)
        # pygame.draw.circle(self.game.screen,
        #                    self.color,
        #                    (self.coordinates.x, self.coordinates.y),
        #                    self.mass ** (1 / 7))

    def force_between(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        force = game.Game.G * ((self.mass * other.mass) / distance ** 2)
        angle = math.atan2(dy, dx)
        x_force = (math.cos(angle) * force / self.mass)
        self.velocity.x += x_force
        self.velocity.y += math.sin(angle) * force / self.mass
