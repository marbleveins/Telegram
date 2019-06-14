import pygame, sys, os
from pygame.locals import *
from classes import *


def main():
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    pygame.display.set_caption('PyGame Snake')

    window = pygame.display.set_mode((480, 480))
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 20)

    game = SnakeGame(window, screen, clock, font)

    while game.run(pygame.event.get()):
        pass

    # pylint: disable=no-member
    pygame.quit()
    # pylint: enable=no-member
    sys.exit()


if __name__ == '__main__':
    main()