import pygame, menu

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