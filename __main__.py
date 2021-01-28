import pygame, time, settings, controller, view
pygame.init()



while True:
    time.sleep(1/60)

    view.create_screen()

    controller.events()