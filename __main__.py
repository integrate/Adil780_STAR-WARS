import pygame, time, settings, controller, view, model
pygame.init()



while True:
    time.sleep(1/60)

    controller.events()

    model.move_enemy_down()



    view.create_screen()

    view.ship_drawing()

