import pygame
from pygame import Surface, Rect
from pygame.math import Vector2
import sys

from body import Body


class Game:
    G = 6.674 * 10 ** -11

    def __init__(self):
        self.__scale: int = 1
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
        pygame.draw.circle(self.screen, sun.color, (sun.coordinates.x, sun.coordinates.y), 10 * self.__scale)

    def tick(self):
        self.clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_COMMA]:
                    self.scale = self.scale / 2
                elif pressed[pygame.K_PERIOD]:
                    self.scale = self.scale * 2

        self.screen.fill((10, 10, 10))

        for body in self.planets:
            for other in self.planets:
                if body == other:
                    continue

                body.force_between(other)

            body.x += body.velocity.x
            body.y += body.velocity.y
            body.draw()

        # self.screen.blit(self.scaled_screen, (0, 0))
        pygame.display.flip()

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if scale >= 1:
            # c, d = self.screen.get_width() / 2, self.screen.get_height() / 2,
            # factor = scale / self.__scale
            # for b in self.planets:
            #     b.coordinates.x = c + factor * (b.coordinates.x - c)
            #     b.coordinates.y = d + factor * (b.coordinates.y - d)

            self.__scale = int(scale)
