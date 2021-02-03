import pygame, settings, random, view

pygame.init()

left_bullet = None
right_bullet = None

ship = pygame.Rect(settings.SCREEN_WIDTH / 2, 650, 101, 110)
ship.centerx = settings.SCREEN_WIDTH / 2

enemy_ship = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 101), 5, 101, 110)

enemy = []

basespeed = 10
speedx = basespeed
speedy = basespeed

bullets = []

def right_bullet_creation():
    right_bullet = pygame.Rect(ship.right, ship.top, 3, 20)
    bullets.append(right_bullet)

def left_bullet_creation():
    left_bullet = pygame.Rect(ship.left, ship.top, 3, 20)
    bullets.append(left_bullet)

def bullets_movement():
    for i in bullets:
        basespeed = 8
        i.y -= basespeed

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
