import sys

import pygame

from game import Game


def main():
    pygame.init()
    pygame.font.init()
    g = Game()
    g.main_loop()
    sys.exit()


if __name__ == '__main__':
    main()
