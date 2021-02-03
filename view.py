import pygame, settings, model


bullet = pygame.image.load("images/bullet 2.png")
bullet = pygame.transform.scale(bullet, [3, 20])

def create_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

def draw_bullets():
    if len(model.bullets) != 0:
        for i in model.bullets:
            #pygame.draw.rect(screen, [255, 255, 255], i, 2)
            screen.blit(bullet, i)

def drawing():
    global screen, bullet
    #pygame.draw.rect(screen, [255, 255, 255], model.ship, 2)
    pygame.draw.rect(screen, [255, 255, 255], model.enemy_ship, 2)

    #if model.left_bullet is not None:
        #pygame.draw.rect(screen, [255, 255, 255], model.left_bullet)

    #if model.right_bullet is not None:
        #pygame.draw.rect(screen, [255, 255, 255], model.right_bullet)

    x_wing = pygame.image.load("images/X-WING.png")

    tie = pygame.image.load("images/TIE.png")
    tie = pygame.transform.scale(tie, [101, 110])
    tie = pygame.transform.rotate(tie, 180)



    screen.blit(tie, model.enemy_ship)
    screen.blit(x_wing, model.ship)

    draw_bullets()

    pygame.display.flip()