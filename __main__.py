import pygame, time, settings, controller, view, model
pygame.init()
pygame.mouse.set_visible(False)
view.create_screen()


while True:
    time.sleep(1/60)

    controller.events()

    model.model()

    view.drawing()

