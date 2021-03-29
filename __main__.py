import pygame, time, settings, controller, view, model, menu, store
pygame.init()
#pygame.mouse.set_visible(False)
view.create_screen()



while True:
    time.sleep(1/60)

    if menu.mode == "MENU":
        model.restart()
        menu.create_screen()
        menu.events()

    elif menu.mode == "STORE":
        store.create_store_screen()
        store.store_events()



    else:
        view.drawing()

        model.model()

        controller.events()

    if model.check_game() == True:
        menu.mode = "MENU"








