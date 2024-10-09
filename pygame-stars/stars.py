import pygame
from pygame.sprite import Sprite, Group
import sys
import random

class Star(Sprite):
    """A class to create a star"""

    def __init__(self, screen, col, x, y, radius):
        super().__init__()
        self.screen = screen
        self.color = col
        self.x = x
        self.y = y
        self.radius = radius
        # Store the time of the last update
        self.last_update = pygame.time.get_ticks()
        # Update screen every 80 milliseconds 
        self.update_delay = 80


    def update(self, stars_list):
        """Draw the star to the screen and handle twinkling"""
        # Change brightness to simulate twinkling
        brightness = random.randint(1, 255)
        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if enough time has passed to update the brightness
        if current_time - self.last_update > self.update_delay:
            # Randomly select a star from the group
            chosen_star = random.choice(stars_list)
            chosen_star.color = (brightness, brightness, brightness)

            # Reset the timer
            self.last_update = current_time

        # Draw the circle to the screen
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        
def main():
    # Setup variables
    screen_width = 1200
    screen_height = 800
    BG_COLOR = (0, 0, 0)
    STAR_COLOR = "white"

    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Starfield")
    
    # Create a sprite group for stars
    stars = Group()

    # Create a list of n stars
    for _ in range(500):
        # random (x, y) positions
        x_pos = random.randint(1, screen_width)
        y_pos = random.randint(1, screen_height)
        # random radius size between 1.0 and 4.0
        star_radius = float(random.randrange(100, 401))/100
        star = Star(screen, STAR_COLOR, x_pos, y_pos, star_radius)
        stars.add(star)

    # Create a list of stars
    stars_list = stars.sprites()

    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
        
        # Set the background color
        screen.fill(BG_COLOR)

        # Draw stars on the screen
        stars.update(stars_list)

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()