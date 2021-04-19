import pygame, store_controller, store, skin, model, store_view, skins

pygame.init()

def buy_skin(skin):
    if model.coin >= skin.price:
        store_view.change_skin(skin.image)

