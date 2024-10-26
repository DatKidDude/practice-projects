import pygame

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image
    

    def get_image(self, frame, width, height, color=None, scale=None):
        """Get the spritesheet image and draw it onto the screen"""
        image = pygame.Surface((width, height)).convert_alpha()
        # sheet: image to blit
        # (0, 0): coordinates to place the sheet on image
        # (0, 0, width, height): Area from the original sprite sheet
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image