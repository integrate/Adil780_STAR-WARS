import pygame, settings, model, time
pygame.init()

letters = pygame.font.SysFont("arial", 40, True)


bullet = pygame.image.load("images/bullet 2.png")
bullet = pygame.transform.scale(bullet, [7, 30])
meteorite = pygame.image.load("images/METEOR.png")
meteorite = pygame.transform.scale(meteorite, [70, 70])
x_wing = pygame.image.load("images/X-WING.png")
tie = pygame.image.load("images/TIE.png")
tie = pygame.transform.scale(tie, [101, 110])
tie = pygame.transform.rotate(tie, 180)
background = pygame.image.load("images/background.jpg")
coin = pygame.image.load("images/COIN.png")
coin = pygame.transform.scale(coin, [50, 50])


pl100 = pygame.image.load("images/Platform 100%.png")
pl100 = pygame.transform.scale(pl100, [settings.SCREEN_WIDTH, 40])

pl75 = pygame.image.load("images/Platform 75%.png")
pl75 = pygame.transform.scale(pl75, [settings.SCREEN_WIDTH, 40])

pl50 = pygame.image.load("images/Platform 50%.png")
pl50 = pygame.transform.scale(pl50, [settings.SCREEN_WIDTH, 40])

pl25 = pygame.image.load("images/Platform 25%.png")
pl25 = pygame.transform.scale(pl25, [settings.SCREEN_WIDTH, 40])

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
    for l in model.meteorite:
        #pygame.draw.rect(screen, [255, 255, 255], l, 2)
        screen.blit(meteorite, l["rect"])

def draw_platform():
    if model.platform_hp == 100:
        screen.blit(pl100, [0, settings.SCREEN_HEIGHT - 40])
    elif model.platform_hp == 75:
        screen.blit(pl75, [0, settings.SCREEN_HEIGHT - 40])
    elif model.platform_hp == 50:
        screen.blit(pl50, [0, settings.SCREEN_HEIGHT - 40])
    elif model.platform_hp == 25:
        screen.blit(pl25, [0, settings.SCREEN_HEIGHT - 40])



def create_coin():
    coins = letters.render(str(model.coin), True, [255, 221, 0])
    screen.blit(coin, (650, 5))
    screen.blit(coins, [700, 5])

def game_over():
    go = letters.render("GAME OVER", True, [255, 0, 0])
    screen.blit(go, [settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2])

def drawing():
    global screen, bullet
    if model.platform_hp > 0:
        screen.blit(background, [0, 0])
        draw_platform()
        screen.blit(x_wing, model.ship)


        draw_enemies()
        draw_bullets()

        create_coin()


    else:
            screen.fill([0, 0, 0])
            game_over()


    pygame.display.flip()

