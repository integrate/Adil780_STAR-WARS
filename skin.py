import pygame
pygame.init()

letters = pygame.font.SysFont("arial", 40, True)




class Skin():
    def __init__(self, posx, posy, image, price):
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [100, 110])
        self.price = price

    def draw(self, screen):
        screen.blit(self.image, [self.posx, self.posy])
        pr = letters.render("Price: " + str(self.price), True, [0, 255, 0])
        screen.blit(pr, [self.posx - 30, self.posy + 120])