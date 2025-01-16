import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # get random split angle
        split_angle = random.uniform(20, 50)
        # rotate killed asteroid velocity by angle in both directions and speed it up 20%
        asteroid_1_velocity = self.velocity.rotate(split_angle) * 1.2
        asteroid_2_velocity = self.velocity.rotate(-split_angle) * 1.2
        # get split asteroid radius
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        # instanciate two new asteroids and set respective velocities
        asteroid_1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_1.velocity = asteroid_1_velocity
        asteroid_2.velocity = asteroid_2_velocity