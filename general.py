import pygame
from config import FPS, Width, Height, white, red, green, black, blue
from enemy import enemy
from Hero import hero
from hp import HP
from Background import background_
from random import randint
from Bullet import bullet

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(('Povestka'))
#pygame.display.set_icon(pygame.image.load("app.bmp")) - setting icon of app

#Main constants
font = pygame.font.Font('/System/Library/Fonts/Apple Symbols.ttf', 30)
font1 = pygame.font.Font('/System/Library/Fonts/Apple Symbols.ttf', 80)
font2 = pygame.font.Font('/System/Library/Fonts/Apple Symbols.ttf', 120)
hp_count = 3
speed = 10
left = right = up = False
hero_death = False
score = 0

#Creating objects of a game
hp_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
Enemy = enemy(-100, enemies)
Hero = hero(400, speed)
background = background_(right, left, speed)
hero_hp = pygame.sprite.Group()
hero_hp.add(HP(620, 1), HP(680, 1), HP(740, 1))
bullets = pygame.sprite.Group()

#Creating enemy in a random place (far enough from hero)
def createenemy(group):
    if Hero.rect.x < 400:
        x = randint(Hero.rect.x + 100, 900)
    else:
        x = randint(-100, Hero.rect.x - 100)
    return enemy(x, group)

#   When hero's bullet collides with enemy - enemy dies
def enemy_shot_check():
    global score
    for enemy in enemies:
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, enemy.rect):
                enemy.kill_()
                bullet.kill()
                createenemy(enemies)
                score += 1

#   When hero collides with enemy, enemy dies and hero loses 1 hp
def hero_collision():
    global hp_count, hero_death
    for enemy in enemies:
        if hp_count == 0:
            hero_death = True
            death_window()
            enemy.kill()
            break
        if pygame.Rect.colliderect(Hero.rect, enemy.rect):
            enemy.kill_()
            createenemy(enemies)
            hp_count -= 1
            for hp in hero_hp:
                hp.kill_()
                break

#   When hp count is zero, game stops and shows user's score
def death_window():
    death = True
    while death:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        txt = font1.render(f'You score is {score}', True, red)
        screen.blit(background.image, background.rect)
        txtRect = txt.get_rect()
        txtRect.center = (400, 300)
        screen.blit(txt, txtRect)
        screen.blit(Hero.image, Hero.rect)

        pygame.display.update()
        background.update(False, False, 0)
        Hero.update(False, False, False, hero_death)
        clock.tick(30)

#   Start window, when user presses 's' button - game starts
def start_window():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start = False
                elif event.key == pygame.K_ESCAPE:
                    exit()
        txt = font1.render('Press s to start', True, red)
        txtRect = txt.get_rect()
        txtRect.center = (410, 250)
        screen.blit(txt, txtRect)
        pygame.display.update()
        clock.tick(30)

#   Game pause: when pause flag is activated, function starts new game cycle that interrupts main cycle
def pause_window():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    exit()
        txt = font1.render('Paused', True, black)
        txtRect = txt.get_rect()
        txtRect.center = (410, 250)
        txt1 = font.render('Press p to continue ', True, black)
        txt1Rect = txt.get_rect()
        txt1Rect.center = (400, 320)
        screen.blit(txt, txtRect)
        screen.blit(txt1, txt1Rect)
        pygame.display.update()
        clock.tick(30)

start_window_flag = True
#Main cycle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_p:
                pause_window()
            if event.key == pygame.K_SPACE:
                bullets.add(bullet(Hero.rect.centerx, Hero.rect.centery, Hero.dir_flag))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_UP:
                up = False

    #Checking collisions
    hero_collision()
    enemy_shot_check()


### Only in alpha version
    #Showing position of objects
    #1st object

    text = font.render('Hero rect' + str(Hero.rect.center), True, black)
    textRect = text.get_rect()
    textRect.topleft = (0, 0)
    #2nd object
    text1 = font.render('Object rect' + str(Enemy.rect.topleft), True, black)
    textRect1 = text.get_rect()
    textRect.topleft = (0, 40)
###

    #Showing object on screen
    screen.fill((0, 0, 0))
    screen.blit(background.image, background.rect)
    hero_hp.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    screen.blit(Hero.image, Hero.rect)
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)

    #Updating object parameters
    pygame.display.update()
    Hero.update(right, left, up, hero_death)
    enemies.update(Hero.rect.centerx)
    bullets.update()
    background.update(right, left, speed)
    if start_window_flag:
        start_window()
        start_window_flag = False

    clock.tick(FPS)