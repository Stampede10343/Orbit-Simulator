import math

from body import Body
from game import Game


def main():
    game = Game()

    while True:
        game.tick()


def orbital_speed(body: Body, center: Body) -> float:
    distance = math.sqrt(
        (body.coordinates.x - center.coordinates.x) ** 2 + (body.coordinates.y - center.coordinates.y) ** 2)
    return math.sqrt(Game.G * (2 / distance - 1 / body.semi_minor_axis))


main()
