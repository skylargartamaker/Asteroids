import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        self.screen = screen
        pygame.draw.polygon(self.screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        r1 = self.radius
        r2 = other.radius
        if distance < r1 + r2:
            return True
        return False