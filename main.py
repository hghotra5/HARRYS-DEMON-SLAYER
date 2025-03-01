import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize Pygame
pygame.init()

# Screen Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HARRYS DEMON SLAYER")

# Load Background Image
background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Resize to fit screen

# Game Entities
player = Player(100, HEIGHT // 2)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player)

# Enemy Spawn Timer
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 2000)  # Spawn every 2 seconds

# Bullet Firing Timer for Rapid Fire
SHOOT_EVENT = pygame.USEREVENT + 2
shooting = False  # Track if spacebar is held down

# Main Loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)  # 30 FPS

    # **Draw Background First**
    screen.blit(background, (0, 0))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Start rapid fire
                shooting = True
                pygame.time.set_timer(SHOOT_EVENT, 200)  # Fire every 200ms
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shooting = False
                pygame.time.set_timer(SHOOT_EVENT, 0)  # Stop firing
        elif event.type == SHOOT_EVENT and shooting:
            bullet = Bullet(player.rect.center, player.direction)
            bullets.add(bullet)
            all_sprites.add(bullet)
        elif event.type == ENEMY_SPAWN_EVENT:  # Spawn new enemy
            enemy = Enemy(WIDTH, random.randint(50, HEIGHT - 50))
            enemies.add(enemy)
            all_sprites.add(enemy)

    # Player Movement
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Update Sprites
    all_sprites.update()

    # Enemy AI: Move toward player
    for enemy in enemies:
        enemy.track_player(player)

    # Collision Detection
    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemy_hit:
            bullet.kill()

    # **Check if Player Collides with an Enemy (Game Over)**
    if pygame.sprite.spritecollideany(player, enemies):
        print("Game Over!")
        running = False  # End the game

    # Draw Sprites **After Background**
    all_sprites.draw(screen)
    pygame.display.flip()



def game_over(screen):
    font = pygame.font.Font(None, 80)  # Choose a font and size
    text = font.render("GAME OVER YOU SUCK", True, (255, 0, 0))  # Red text
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    screen.fill((0, 0, 0))  # Fill screen with black
    screen.blit(text, text_rect)  # Draw "Game Over" text
    pygame.display.flip()  # Update display

    pygame.time.delay(3000)  # Wait for 3 seconds
    pygame.quit()  # Close the game
    exit()
    


pygame.quit()
