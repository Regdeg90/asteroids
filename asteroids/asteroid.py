import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(surface=screen, color="white", radius=self.radius, center=self.position, width=2)
    
    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vec1 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(angle)
        vec2 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        ass1 = Asteroid(self.position.x, self.position.y, new_rad)
        ass1.velocity = vec1 * 1.02

        ass2 = Asteroid(self.position.x, self.position.y, new_rad)
        ass2.velocity = vec2 * 1.02