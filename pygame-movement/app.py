import pygame, sys, os
from pygame.sprite import Sprite
import spritesheet


# Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

# Colors 
BG = (50, 50, 50)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Set up the pygame window and set caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Physics")

# Load in ground image
ground = pygame.image.load(os.path.join("assets", "base.png"))
ground = pygame.transform.scale(ground, (SCREEN_WIDTH, ground.get_height()))

# Load in the spritesheet and create a sprite sheet instance
sprite_sheet_image = pygame.image.load(os.path.join("assets", "sprites", "_Run.png")).convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# create animation list
animation_list = []
animation_steps = 10
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 120, 80, BLACK, 2))

# Initialize clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Update background
    screen.fill(BG)
    screen.blit(ground, (0, 700))

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame = (frame + 1) % animation_steps
        last_update = current_time

    # Show frame image at pos (x,y)
    screen.blit(animation_list[frame], (0, 545))

    # Update the screen
    pygame.display.flip()
    # Limit framerate
    clock.tick(FPS)

pygame.quit()
sys.exit()