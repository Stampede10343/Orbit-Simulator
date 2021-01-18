from game import Game


def main():
    game = Game()

    while game.alive:
        game.tick()


main()
