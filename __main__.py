import pygame, time, settings, controller, view, model
pygame.init()




while True:
    time.sleep(1/60)

    controller.events()

    model.move_enemy_down()

    model.bullets_movement()



    view.create_screen()

    view.drawing()

