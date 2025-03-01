import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def track_player(self, player):
        """ Move towards the player """
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx, dy = dx / distance, dy / distance  # Normalize
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
