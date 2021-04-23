import pygame, tkinter
pygame.init()

letters = pygame.font.SysFont("arial", 40, True)




class Skin():
    def __init__(self, posx, posy, image, price):
        self.posx = posx
        self.posy = posy
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [100, 110])
        self.price = price
        self.pr = letters.render("Price: " + str(self.price), True, [0, 255, 0])
        self.rect = pygame.Rect(self.posx, self.posy, 100, 110)
        self.rect_price = pygame.Rect(self.posx - 30, self.posy + 120, self.pr.get_width(), self.pr.get_height())
        self.sold = False


    def draw(self, screen):
        if self.sold:
            self.bought = letters.render("BOUGHT", True, [0, 0, 255])
            screen.blit(self.bought, [self.posx - 30, self.posy + 120])

        else:
            screen.blit(self.pr, [self.posx - 30, self.posy + 120])




        screen.blit(self.image, [self.posx, self.posy])

        #pygame.draw.rect(screen, [255, 0, 0], self.rect, 2)
        #pygame.draw.rect(screen,[255, 0, 0], self.rect_price, 2)

    def collide_possition(self, pos):
        if self.rect.collidepoint(pos) or self.rect_price.collidepoint(pos):
            return True

        else:
            return False


