import pygame, settings, menu, skins, model, view, store
pygame.init()

price = []
skin = []



letters = pygame.font.SysFont("arial", 40, True)



# for i in skins.skins:
#     rect = pygame.Rect(50, settings.SCREEN_WIDTH - 50, 110, 100)
#     skin1 = pygame.image.load(i["image"])
#     prices = i["price"]
#     pr = letters.render("Price: " + str(prices), True, [255, 0, 0])
#     price.append(pr)
#     skin1 = pygame.transform.scale(skin1, [100, 110])
#     skin.append(skin1)



def create_coin():
    coins = letters.render(str(model.coin), True, [255, 221, 0])
    screen.blit(view.coin, [650, 5])
    screen.blit(coins, [700, 5])




def cretion_skins():
    # skin_num = 0
    # price_num = 0
    # for y in range(50, settings.SCREEN_HEIGHT - 50, 250):
    #     for f in range(50, settings.SCREEN_WIDTH - 50, 180):
    #         if len(skin) <= skin_num:
    #             return
    #         skin_save = skin[skin_num]
    #         screen.blit(skin_save, [f, y])
    #         skin_num += 1

    #         price_save = price[price_num]
    #         screen.blit(price_save, [f - 30, y + 120])
    #         price_num += 1

    for i in store.sk1n:
        i.draw(screen)


def change_skin(skin):
    view.x_wing = skin



def create_store_screen():
    global screen
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    screen.fill([0, 0, 0])
    cretion_skins()
    create_coin()

    pygame.display.flip()