import pygame
pygame.init()

ship = pygame.Rect(900, 650, 101, 110)

speedx = 10
speedy = 10

def move_ship_right():
    ship.x += 10
def move_ship_left():
    ship.x -= 10