import pygame
pygame.init()

class Skin():
    def __init__(self, posx, posy, image):
        self.image = image
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load(image)

    def draw(self, screen):
        screen.blit(self.image, [self.posx, self.posy])

