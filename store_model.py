import pygame, model, store_view, utils, view

pygame.init()

def buy_skin(skin):
    if skin.sold:
        if utils.ask_yes_no(message="Do you want to change your skin?"):
            store_view.change_skin(skin.image)
            return
    if model.coin >= skin.price:
        if utils.ask_yes_no(message="Are you sure?"):
            model.coin -= skin.price
            store_view.change_skin(skin.image)
            view.x_wing_id = skin.id
            skin.sold = True


    else:
        utils.show_warning()

def sold_skin0(skin):
    if skin.price <= 0:
        skin.sold = True






