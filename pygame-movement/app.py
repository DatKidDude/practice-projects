import pygame, sys
from pygame.sprite import Sprite


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

# Initialize pygame
pygame.init()

# Set up the pygame window and set caption
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Physics")

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

    screen.fill("green")

    # Update the screen
    pygame.display.flip()
    # Limit framerate
    clock.tick(FPS)

pygame.quit()
sys.exit()