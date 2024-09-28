from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.posit = (x, y)
        self.radius = radius
    

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.posit, self.radius, width = 2)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.posit += forward * PLAYER_SPEED * dt
        