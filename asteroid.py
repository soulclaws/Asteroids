import pygame
import random
from constants import *
from circleshape import *
from logger import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
         pygame.draw.circle(screen, "grey", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else :
            log_event("asteroid_split")
            rand_float = random.uniform(20, 50)
            vector1 = self.velocity.rotate(rand_float)
            vector2 = self.velocity.rotate(rand_float) * -1
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
