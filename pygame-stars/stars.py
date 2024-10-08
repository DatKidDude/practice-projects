import pygame
import sys


def main():
    # Setup variables
    screen_width = 1200
    screen_height = 800
    BG_COLOR = (0, 0, 0)

    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Starfield")

    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Set the background color
        screen.fill(BG_COLOR)

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()