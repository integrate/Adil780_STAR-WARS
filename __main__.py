import pygame, tkinter,  time, settings, controller, view, model, menu, store_view, store_controller, store

pygame.init()
#pygame.mouse.set_visible(False)
view.create_screen()

from tkinter import messagebox

#messagebox.showwarning(message="Hello")
#messagebox.askyesno(message="Hello")




while True:
    time.sleep(1/60)

    if menu.mode == "MENU":
        model.restart()
        menu.create_screen()
        menu.events()

    elif menu.mode == "STORE":
        store_view.create_store_screen()
        store_controller.store_events()



    else:
        view.drawing()

        model.model()

        controller.events()

    if model.check_game() == True:
        menu.mode = "MENU"








