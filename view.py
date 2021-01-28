import pygame, settings, model

def create_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

def ship_drawing():
    global screen
    pygame.draw.rect(screen, [255, 255, 255], model.ship, 2)
    x_wing = pygame.image.load("images/X-WING.png")
    screen.blit(x_wing, model.ship)
    pygame.display.flip()