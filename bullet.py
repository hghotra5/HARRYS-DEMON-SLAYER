import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 10
        self.direction = direction  # The direction the bullet will move

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        if self.rect.x > 800 or self.rect.x < 0 or self.rect.y > 600 or self.rect.y < 0:
            self.kill()
