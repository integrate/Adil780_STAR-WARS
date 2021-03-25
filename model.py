import pygame, settings, random, view

pygame.init()



left_bullet = None
right_bullet = None

ship = pygame.Rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - 150, 101, 110)
ship.centerx = settings.SCREEN_WIDTH / 2

platform = pygame.Rect(0, settings.SCREEN_HEIGHT - 40, settings.SCREEN_WIDTH, 40)

letters = pygame.font.SysFont("arial", 40, True)


speedx = 10
speedy = 10


platform_hp = 100
coin = 0

enemy = []
bullets = []
meteorite = []


#BULLET

def right_bullet_creation():
    right_bullet = pygame.Rect(ship.right, ship.top, 3, 20)
    if len(bullets) < 5:
        bullets.append(right_bullet)

def left_bullet_creation():
    left_bullet = pygame.Rect(ship.left, ship.top, 3, 20)
    if len(bullets) < 5:
        bullets.append(left_bullet)

def bullet_remove():
    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)

def bullets_movement():
    for i in bullets:
        basespeed = 15
        i.y -= basespeed



#SHIP

def move_ship_right():
    ship.x += 10
    correct_borders()

def move_ship_to(posx):
    ship.centerx = posx
    correct_borders()

def correct_borders():
    if ship.right >= settings.SCREEN_WIDTH:
        ship.right = settings.SCREEN_WIDTH
    if ship.left <= 0:
        ship.left = 0

def move_ship_left():
    ship.x -= 10
    correct_borders()

#ENEMY

def create_enemy():
    global enemy_ship
    enemy_ship = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 101), 5, 101, 110)
    enemy.append(enemy_ship)

def move_enemy_down():
    global speedy
    for i in enemy:
        speedy = 10
        i.y += speedy

#METEORITE

def create_meteorite():
    global speedy, speedx
    meteorit_e = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 70), 5, 70, 70)
    m = {"rect":meteorit_e, "speedy":random.randint(1, 5), "speedx":random.randint(-5, 5)}
    meteorite.append(m)
    speedx = random.randint(-5, 5)
    speedy = random.randint(1, 2)


def move_meteorite_down():
    global speedy, speedx
    for i in meteorite:
        i["rect"].y += i["speedy"]
        i["rect"].x += i["speedx"]


#COLLIDE

def collide_bullet_meteorite():
    for i in meteorite.copy():
        a = i["rect"].collidelist(bullets)
        if a > -1:
            meteorite.remove(i)
            del bullets[a]


def collide_bullet_enemy():
    global coin
    for i in enemy.copy():
        a = i.collidelist(bullets)
        if a > -1:
            enemy.remove(i)
            del bullets[a]
            coin += 1

def collide_platform_meteorite():
    global platform_hp
    for i in meteorite:
        a = platform.colliderect(i["rect"])
        if a == 1:
            meteorite.remove(i)
            platform_hp -= 25

def collide_platform_enemy():
    global platform_hp
    a = platform.collidelistall(enemy)
    for i in a.copy():
        del enemy[i]
        platform_hp -= 25


def check_game():
    if platform_hp <= 0:
        return True
    else:
        return False

def restart():
    global platform_hp, coin
    platform_hp = 100
    coin = 0


#MODEL

def model():
    move_enemy_down()
    move_meteorite_down()
    bullets_movement()
    collide_bullet_enemy()
    collide_bullet_meteorite()
    bullet_remove()
    collide_platform_meteorite()
    collide_platform_enemy()
    #collide_platform_enemy(meteorite)
