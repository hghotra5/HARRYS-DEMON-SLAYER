import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.direction = (1, 0)  # Default: right

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = (0, -1)
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = (0, 1)
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = (-1, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = (1, 0)
