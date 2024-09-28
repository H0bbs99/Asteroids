from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.posit = (x, y)
        self.radius = radius
    

    def draw(self, dt):
        pygame.draw.circle(screen, (255, 255, 255), self.posit, self.radius, width = 2)
    
    def update(self, screen):
