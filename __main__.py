import pygame, time, settings, controller, view, model
pygame.init()



while True:
    time.sleep(1/60)

    view.create_screen()

    controller.events()

    view.ship_drawing()

