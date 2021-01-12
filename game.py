import math
import pygame
from pygame import Surface, Rect
from pygame.math import Vector2
import sys

from body import Body


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
        sun = Body(
            mass=400000000000,
            semi_minor_axis=0,
            coordinates=Rect(
                (self.screen.get_width() / 2),
                (self.screen.get_height() / 2),
                0,
                0),
            velocity=Vector2())
        earth = Body(
            mass=10000,
            semi_minor_axis=149.596,
            coordinates=Rect(420, 240, 0, 0),
            velocity=Vector2(0.2, -0.2))

        return [sun, earth]

    def force_between(self, earth: Body, sun: Body):
        dx = earth.x - sun.x
        dy = earth.y - sun.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        force = Game.G * ((earth.mass * sun.mass) / distance ** 2)
        angle = math.atan2(dy, dx)
        x_force = (math.cos(angle) * force / earth.mass)
        earth.velocity.x -= x_force
        earth.velocity.y -= math.sin(angle) * force / earth.mass
        sun.velocity.x -= math.cos(angle) * force / sun.mass
        sun.velocity.y -= math.sin(angle) * force / sun.mass

    def draw_sun(self):
        sun = self.planets[0]
        pygame.draw.circle(self.screen, (200, 255, 255), (sun.x, sun.y), 10)

    def tick(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.screen.fill((0, 0, 0))

        earth = self.planets[1]
        sun = self.planets[0]
        self.force_between(earth, sun)
        # earth.coordinates = earth.coordinates.move(earth.velocity.x, earth.velocity.y)
        earth.x += earth.velocity.x
        earth.y += earth.velocity.y
        earth.coordinates.x = earth.x
        earth.coordinates.y = earth.y

        sun.x += sun.velocity.x
        sun.y += sun.velocity.y
        sun.coordinates.x = sun.x
        sun.coordinates.y = sun.y
        # sun.coordinates = sun.coordinates.move(sun.velocity.x, sun.velocity.y)
        self.draw_sun()
        er = earth.coordinates

        pygame.draw.circle(self.screen, (180, 180, 180), (er.x, er.y), 8)
        pygame.display.flip()
