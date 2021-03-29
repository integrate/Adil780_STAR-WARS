import pygame, settings

pygame.init()


#CONTROLLER

def events():
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
            xy = i.pos
            press_play_button(xy)
            press_store_button(xy)






#MODEL

play_button = pygame.Rect(0, settings.SCREEN_HEIGHT - 400, 400, 200)
store_button = pygame.Rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - 400, 400, 200)

mode = "MENU"

def press_play_button(click):
    global mode
    a = play_button.collidepoint(click)
    if a == 1:
        mode = "GAME"
        print("Play")


def press_store_button(click):
    global mode
    a = store_button.collidepoint(click)
    if a == 1:
        mode = "STORE"
        print("Store")




#VIEW

word = pygame.font.SysFont("arial", 150, True)




def create_button(text, color, rect):
    pygame.draw.rect(screen, color, rect)
    button = word.render(text, True, [0, 0, 0])
    w = button.get_width()
    h = button.get_height()
    screen.blit(button, [(rect.width - w) / 2 + rect.left, (rect.height - h) /2 + rect.top])






def create_screen():
        global screen
        screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        screen.fill([0, 0, 0])



        create_button("Play", [255, 0, 0], play_button)
        create_button("Store", [0, 0, 255], store_button)


        pygame.display.flip()