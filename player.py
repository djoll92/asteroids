import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.fire_rate = 0

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

    def shoot(self):
        if self.fire_rate > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.fire_rate = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        self.fire_rate -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()