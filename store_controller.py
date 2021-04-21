import pygame, menu, store, store_model



def store_events():

    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                menu.mode = "MENU"

        if i.type == pygame.MOUSEMOTION:
            a = i.pos
            skiins = False
            for p in store.sk1n:
                b = p.collide_possition(a)
                if b:
                    skiins = True
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)

                if skiins == False:
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)


        if i.type == pygame.MOUSEBUTTONDOWN:
            a = i.pos
            for p in store.sk1n:
                b = p.collide_possition(a)
                if b:
                    store_model.buy_skin(p)





