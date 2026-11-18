import pygame
import sys
from asteroid import Asteroid
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astobject = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0.0




    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()


        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
