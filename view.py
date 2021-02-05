import pygame, settings, model


bullet = pygame.image.load("images/bullet 2.png")
bullet = pygame.transform.scale(bullet, [3, 20])

tie = pygame.image.load("images/TIE.png")
tie = pygame.transform.scale(tie, [101, 110])
tie = pygame.transform.rotate(tie, 180)

def create_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])

def draw_bullets():
    for i in model.bullets:
        #pygame.draw.rect(screen, [255, 255, 255], i, 2)
        screen.blit(bullet, i)

def draw_enemies():
    for i in model.enemy:
        #pygame.draw.rect(screen, [255, 255, 255], i, 2)
        screen.blit(tie, i)

def drawing():
    global screen, bullet
    x_wing = pygame.image.load("images/X-WING.png")
    screen.blit(x_wing, model.ship)

    draw_enemies()
    draw_bullets()

    pygame.display.flip()

