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
    skin_num = 0
    price_num = 0
    for y in range(50, settings.SCREEN_HEIGHT - 50, 250):
        for f in range(50, settings.SCREEN_WIDTH - 50, 180):
            if len(skin) <= skin_num:
                return
            skin_save = skin[skin_num]
            screen.blit(skin_save, [f, y])
            skin_num += 1
            price_save = price[price_num]
            screen.blit(price_save, [f - 30, y + 120])
            price_num += 1





def create_store_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    screen.fill([0, 0, 0])
    cretion_skins()







    pygame.display.flip()