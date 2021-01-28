import pygame, model
pygame.init()

pygame.key.set_repeat(20)
def events():
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                model.move_ship_right()
            if i.key == pygame.K_LEFT:
                model.move_ship_left()


