import pygame, time, settings, controller, view, model
pygame.init()




while True:
    time.sleep(1/60)

    controller.events()

    model.model()

    view.create_screen()

    view.drawing()

