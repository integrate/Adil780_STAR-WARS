import pygame, settings, random

pygame.init()

bullet = None

ship = pygame.Rect(settings.SCREEN_WIDTH / 2, 650, 101, 110)
ship.centerx = settings.SCREEN_WIDTH / 2

enemy_ship = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 101), 5, 101, 110)

enemy = []

basespeed = 10
speedx = basespeed
speedy = basespeed


def bullet_creation():
    global bullet
    bullets = []
    bullet = pygame.Rect(ship.left, ship.top, 5, 5)

def bullet_movement():
    if bullet is not None:
        bullet.y -= speedy



def move_ship_right():
    ship.x += 10
    if ship.right >= settings.SCREEN_WIDTH:
        ship.right = settings.SCREEN_WIDTH


def move_ship_left():
    ship.x -= 10
    if ship.left <= 0:
        ship.left = 0


def move_enemy_down():
    global basespeed
    basespeed = 3
    enemy_ship.y += speedy
