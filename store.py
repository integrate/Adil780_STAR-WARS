import pygame, settings
pygame.init()


#CONTROLLER

def store_events():
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

#VIEW

skin = []

skin2 = pygame.image.load("images/Skin2.png")
skin2 = pygame.transform.scale(skin2, [101, 110])
skin.append(skin2)

skin1 = pygame.image.load("images/skin1.png")
skin1 = pygame.transform.scale(skin1, [101, 110])
skin.append(skin1)

def cretion_skins():
    cordinatex = 50
    cordinatey = 500
    for p in skin:
        cordinatex += 150
        screen.blit(p, [cordinatex, cordinatey])



def create_store_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    screen.fill([0, 0, 0])
    cretion_skins()







    pygame.display.flip()