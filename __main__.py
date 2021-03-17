import pygame, time, settings, controller, view, model, view_menu, controller_menu
pygame.init()
#pygame.mouse.set_visible(False)
view.create_screen()

mode = "MENU"




if mode == "MENU":
    while True:
        view_menu.create_screen()
        controller_menu.events()




if mode == "GAME":
    while True:
        time.sleep(1/60)

        model.model()

        controller.events()

        view.drawing()

