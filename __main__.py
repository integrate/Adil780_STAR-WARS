import pygame, time, settings, controller, view, model, view_menu, controller_menu
pygame.init()
#pygame.mouse.set_visible(False)
view.create_screen()


while view_menu.mode == "MENU":
    view_menu.create_screen()
    view_menu.events()


if view_menu.mode == "GAME":
    while True:
        time.sleep(1/60)

        view.drawing()

        model.model()

        controller.events()



