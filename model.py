import pygame, settings, random, view

pygame.init()

left_bullet = None
right_bullet = None

ship = pygame.Rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - 150, 101, 110)
ship.centerx = settings.SCREEN_WIDTH / 2

platform = pygame.Rect(0, settings.SCREEN_HEIGHT - 40, settings.SCREEN_WIDTH, 40)


speedx = 10
speedy = 10


platform_hp = 100


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
    print(len(bullets))

def move_enemy_down():
    global speedy
    for i in enemy:
        speedy = 10
        i.y += speedy

#METEORITE

def create_meteorite():
    meteorit_e = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 70), 5, 70, 70)
    meteorite.append(meteorit_e)

def move_meteorite_down():
    global speedy, speedx
    for i in meteorite:
        speedx = random.randint(-5, 5)
        speedy = random.randint(0, 5)
        i.y += speedy
        i.x += speedx

#COLLIDE

def collide_bullet_enemy(enemies):
    for i in enemies.copy():
        a = i.collidelist(bullets)
        if a > -1:
            enemies.remove(i)
            del bullets[a]


def collide_platform_enemy(enemies):
    global platform_hp
    a = platform.collidelistall(enemies)
    for i in a:
        b = enemies[i]
        enemies.remove(b)
        platform_hp -= 25



#MODEL

def model():
    move_enemy_down()
    move_meteorite_down()
    bullets_movement()
    collide_bullet_enemy(enemy)
    collide_bullet_enemy(meteorite)
    bullet_remove()
    collide_platform_enemy(enemy)
    collide_platform_enemy(meteorite)
    print(len(bullets))
