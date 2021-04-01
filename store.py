import pygame, settings, menu, skins
pygame.init()


#CONTROLLER

def store_events():
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                menu.mode = "MENU"

#VIEW

skin = []
price = []

letters = pygame.font.SysFont("arial", 40, True)

for i in skins.skins:
    skin1 = pygame.image.load(i["image"])
    prices = i["price"]
    pr = letters.render("Price: " + str(prices), True, [255, 0, 0])
    price.append(pr)
    skin1 = pygame.transform.scale(skin1, [100, 110])
    skin.append(skin1)



def cretion_skins():
    cordinatex = 50
    cordinatey = 500
    for p in skin:
        cordinatex += 180
        screen.blit(p, [cordinatex, cordinatey])

    cordinatex = 20
    cordinatey = 650
    for k in price:
        cordinatex += 180
        screen.blit(k, [cordinatex, cordinatey])


def create_store_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    screen.fill([0, 0, 0])
    cretion_skins()







    pygame.display.flip()