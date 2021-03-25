import pygame, time, settings, controller, view, model, view_menu, controller_menu
pygame.init()
#pygame.mouse.set_visible(False)
view.create_screen()



while True:
    time.sleep(1/60)

    if view_menu.mode == "MENU":
        model.restart()
        view_menu.create_screen()
        view_menu.events()
    else:
        view.drawing()

        model.model()

        controller.events()

    if model.check_game() == True:
        view_menu.mode = "MENU"








