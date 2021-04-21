import pygame, model, store_view, utils

pygame.init()

def buy_skin(skin):
    if model.coin >= skin.price:
        if utils.ask_yes_no():
            model.coin -= skin.price
            store_view.change_skin(skin.image)
    else:
        utils.show_warning()


