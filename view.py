import pygame, settings, model




bullet = pygame.image.load("images/bullet 2.png")
bullet = pygame.transform.scale(bullet, [7, 30])
x_wing = pygame.image.load("images/X-WING.png")
tie = pygame.image.load("images/TIE.png")
tie = pygame.transform.scale(tie, [101, 110])
tie = pygame.transform.rotate(tie, 180)
background = pygame.image.load("images/background.jpg")
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

def draw_platform():
    if model.platform_hp == 100:
        pygame.draw.rect(screen, [0, 255, 0], model.platform)
    elif model.platform_hp == 75:
        pygame.draw.rect(screen, [255, 234, 8], model.platform)
    elif model.platform_hp == 50:
        pygame.draw.rect(screen, [255, 144, 1], model.platform)
    elif model.platform_hp == 25:
        pygame.draw.rect(screen, [255, 0, 65], model.platform)

def drawn_explotion():
    explotion = pygame.image.load("images/EXPLOTION.png")
    screen.blit(explotion, [140, 100])

def drawing():
    global screen, bullet
    screen.blit(background, [0, 0])
    screen.blit(x_wing, model.ship)

    draw_enemies()
    draw_bullets()
    draw_platform()
    drawn_explotion()

    pygame.display.flip()

