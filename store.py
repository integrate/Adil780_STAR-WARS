import pygame, skin, skins, settings, store_model
pygame.init()

sk1n = []


skin_num = 0
for y in range(50, settings.SCREEN_HEIGHT - 50, 250):
    for f in range(50, settings.SCREEN_WIDTH - 50, 180):

        if len(skins.skins) <= skin_num:
            break
        skin_save = skins.skins[skin_num]
        sk1n.append(skin.Skin(f, y, skin_save["image"], skin_save["price"]))
        skin_num += 1

for i in sk1n:
    store_model.sold_skin0(i)







