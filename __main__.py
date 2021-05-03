import pygame, tkinter,  time, json, controller, view, model, menu, store_view, store_controller, skins, os, store, skin

pygame.init()

if os.path.exists("save.json"):
    f = open("save.json", "r")
    a = json.load(f)
    model.coin = a["coin"]
    view.x_wing = a["SKIN_ID"]
    for i in store.sk1n:
        if i.id in a["bought_skins_id"]:
            i.sold = True
    #store. = a["bought_skin_id"]
    for i in store.sk1n:
        if view.x_wing == i.id:
            view.x_wing = i.image



#pygame.mouse.set_visible(False)
view.create_screen()


from tkinter import messagebox

r = tkinter.Tk()
r.withdraw()

#messagebox.showwarning(message="You don't have enough coins!")
#messagebox.askyesno(message="Are you sure?")




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








