import pygame
from pygame.sprite import Sprite, Group
import sys
import random


class Raindrop(Sprite):
    """Class to create a raindrop"""

    def __init__(self, screen, x, speed):
        super().__init__()
        self.screen = screen

        # Load the raindrop image and get its rect attribute
        self.image = pygame.image.load("images/raindrop.png").convert_alpha()
        # Scale the image size down
        self.image = pygame.transform.scale(self.image, (30, 60))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()

        # Start each raindrop at the top of the screen
        self.rect.x = x
        self.rect.top = 0
        # Store raindrop y position as a float to get more variation in speed
        self.y = float(self.rect.y)

        # Raindrop speed factor
        self.raindrop_speed_factor = speed
        


    def blitme(self):
        """Draw the raindrop"""
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """Make the raindrop fall down the screen"""
        self.y += self.raindrop_speed_factor
        self.rect.y = self.y


def create_raindrops(raindrops, max_raindrops, screen, screen_width):
    """Create more raindrops"""
    print(len(raindrops))
    if len(raindrops) < max_raindrops:
        raindrop_x_pos = random.randint(1, screen_width - 100)
        raindrop_speed_factor = float(random.randint(100, 200))/100
        new_raindrop = Raindrop(screen, raindrop_x_pos, raindrop_speed_factor)
        raindrops.add(new_raindrop)


def remove_raindrops(raindrops, screen_height):
    """Remove raindrops from the group"""
    raindrops.update()

    for raindrop in raindrops.copy():
        if raindrop.rect.top >= screen_height:
            raindrops.remove(raindrop)


def main():
     # Setup variables
    screen_width = 1200
    screen_height = 800
    BG_COLOR = (36, 110, 166)
    MAX_RAINDROPS = 10

    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Raindrops")

    # Create a group for raindrops
    raindrops = Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Screen background color
        screen.fill(BG_COLOR)

        # Create raindrops
        create_raindrops(raindrops, MAX_RAINDROPS, screen, screen_width)

        # Remove raindrops 
        remove_raindrops(raindrops, screen_height)

        raindrops.draw(screen)

        # Update the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()