import pygame, skin, skins
pygame.init()

sk1n = []

for i in skins.skins:
    sk1n.append(skin.Skin(115, 200, i["image"]))


