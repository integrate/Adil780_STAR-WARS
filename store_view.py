import pygame, settings, menu, skins, model, view, store, skin
pygame.init()

price = []




letters = pygame.font.SysFont("arial", 40, True)


def create_coin():
    coins = letters.render(str(model.coin), True, [255, 221, 0])
    screen.blit(view.coin, [650, 5])
    screen.blit(coins, [700, 5])




def cretion_skins():
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