import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            a = self.velocity.rotate(new_angle)
            b = self.velocity.rotate(-new_angle)

            split_asteroid1 = Asteroid(self.position.x, self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
            split_asteroid2 = Asteroid(self.position.x, self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
            split_asteroid1.velocity = a * 1.2
            split_asteroid2.velocity = b * 1.2


        