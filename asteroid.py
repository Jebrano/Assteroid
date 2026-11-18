import circleshape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "White", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ang = random.uniform(20, 50)
            ast1a = self.velocity.rotate(ang)
            ast2a = self.velocity.rotate(-ang)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0], self.position[1], new_radius)
            ast2 = Asteroid(self.position[0], self.position[1], new_radius)
            ast1.velocity = ast1a * 1.2
            ast2.velocity = ast2a * 1.2
