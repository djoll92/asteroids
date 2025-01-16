import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        # determine vector direction and orientation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # determine vector direction and orientation and downscale it's intensity
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        # top (bottom) vertex is positioned in determiend direction/orientation with the intensity of hitbox radius
        a = self.position + forward * self.radius

        # left vertex - move it top in the forward direction and then left by scaled intensity
        b = self.position - forward * self.radius - right

        # right vertex - move it top in the forward direction and then right by scaled intensity
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # determine vector direction and orientation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # reposition in determined direction with scaled intensity (speed)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)