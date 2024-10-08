import pygame
import sys


class Star:
    """A class to create a star"""

    def __init__(self, screen):
        self.surface = screen
        self.color = (255, 255, 255)
        self.center = (600, 400)
        self.radius = 100
    

    def draw_star(self):
        """Draw the star to the screen"""
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)



def main():
    # Setup variables
    screen_width = 1200
    screen_height = 800
    BG_COLOR = (0, 0, 0)

    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Starfield")

    star = Star(screen)

    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Set the background color
        screen.fill(BG_COLOR)

        star.draw_star()

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()