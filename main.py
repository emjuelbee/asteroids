import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        updatable.update(dt)


if __name__ == "__main__":
    main()
