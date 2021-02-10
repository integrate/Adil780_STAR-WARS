import pygame, model
pygame.init()

TIMER_ID = pygame.event.custom_type()
pygame.time.set_timer(TIMER_ID, 1000, 0)
pygame.key.set_repeat(20)
def events():

    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.MOUSEMOTION:
            a = i.pos[0]
            model.move_ship_to(a)

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d:
                model.move_ship_right()
            if i.key == pygame.K_a:
                model.move_ship_left()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                model.left_bullet_creation()

            if i.button == 3:
                model.right_bullet_creation()


        if i.type == TIMER_ID:
            model.create_enemy()






