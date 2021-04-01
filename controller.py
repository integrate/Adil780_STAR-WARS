import pygame, model, menu
pygame.init()

TIMER_ID_ENEMY = pygame.event.custom_type()
TIMER_ID_METEORITE = pygame.event.custom_type()
pygame.time.set_timer(TIMER_ID_ENEMY, 1000, 0)
pygame.time.set_timer(TIMER_ID_METEORITE, 4000, 0)
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
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    menu.mode = "MENU"
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                model.left_bullet_creation()

            if i.button == 3:
                model.right_bullet_creation()



        if i.type == TIMER_ID_ENEMY:
            model.create_enemy()
        if i.type == TIMER_ID_METEORITE:
            model.create_meteorite()






