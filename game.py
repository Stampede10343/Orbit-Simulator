import math
import pygame
from pygame import Surface, Rect
from pygame.math import Vector2
import sys

from body import Body


def force_between(earth: Body, sun: Body):
    dx = earth.x - sun.x
    dy = earth.y - sun.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    force = Game.G * ((earth.mass * sun.mass) / distance ** 2)
    angle = math.atan2(dy, dx)
    x_force = (math.cos(angle) * force / earth.mass)
    earth.velocity.x -= x_force
    earth.velocity.y -= math.sin(angle) * force / earth.mass


class Game:
    G = 6.674 * 10 ** -11

    def __init__(self):
        self.scale: float = 0.5
        self.time_scale = 1
        pygame.init()
        self.screen: Surface = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.planets = self.create_planets()

    def create_planets(self) -> [Body]:
        sun = Body(mass=400000000000,
                   coordinates=Rect((self.screen.get_width() / 2),
                                    (self.screen.get_height() / 2),
                                    10,
                                    10),
                   velocity=Vector2(),
                   game_instance=self,
                   color=(200, 245, 25))
        return [
            sun,
            Body(
                mass=10000,
                coordinates=Rect(420, 240, 9, 9),
                velocity=Vector2(0.08, -0.05),
                game_instance=self,
                color=(50, 220, 100)),
            Body(
                mass=10000000,
                coordinates=Rect(sun.coordinates.x, 140, 10, 10),
                velocity=Vector2(0.2, 0.05),
                game_instance=self),
            Body(
                mass=10000,
                coordinates=Rect(sun.coordinates.x, 190, 10, 10),
                velocity=Vector2(0.10, -0.01),
                game_instance=self)
        ]

    def draw_sun(self):
        sun = self.planets[0]
        pygame.draw.circle(self.screen, sun.color, (sun.x, sun.y), 10)

    def tick(self):
        self.clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.screen.fill((10, 10, 10))

        for body in self.planets:
            for other in self.planets:
                if body == other:
                    continue

                force_between(body, other)
                body.x += body.velocity.x
                body.y += body.velocity.y
                body.coordinates.x = body.x
                body.coordinates.y = body.y
            pygame.draw.circle(self.screen, body.color, (body.coordinates.x, body.coordinates.y), 8)

        self.draw_sun()
        pygame.display.flip()
