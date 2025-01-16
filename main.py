# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.display.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            # quit game and display module if quit event is triggered
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return

        screen.fill("#000000")

        for sprite in updatable:
            sprite.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()
        
        for sprite in drawable:
            sprite.draw(screen)

        # refresh screen drawing
        pygame.display.flip()

        # delta t - actual duration of last frame execution in seconds - frames limited at 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()