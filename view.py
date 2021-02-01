import pygame, settings, model

def create_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])



def drawing():
    global screen
    #pygame.draw.rect(screen, [255, 255, 255], model.ship, 2)
    pygame.draw.rect(screen, [255, 255, 255], model.enemy_ship, 2)
    if model.bullet is not None:
        pygame.draw.rect(screen, [255, 255, 255], model.bullet)
    x_wing = pygame.image.load("images/X-WING.png")
    tie = pygame.image.load("images/TIE.png")
    tie = pygame.transform.scale(tie, [101, 110])
    tie = pygame.transform.rotate(tie, 180)
    screen.blit(tie, model.enemy_ship)
    screen.blit(x_wing, model.ship)
    pygame.display.flip()