import pygame

class hero(pygame.sprite.Sprite):
    def __init__(self, x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.pic1 = pygame.image.load('Hero.png').convert_alpha()
        self.pic2 = pygame.image.load('jump.png').convert_alpha()
        self.pic3 = pygame.image.load('hero_death1.png').convert_alpha()
        self.image = self.pic1
        self.rect = self.image.get_rect(midbottom = (x, 590))
        self.speed = speed
        self.yspeed = 0
        self.dir_flag = False
    def update(self, right, left, up, herodeath):

        # Image mirroring based on movement direction
        if right and right != self.dir_flag:
            self.pic1 = pygame.transform.flip(self.pic1, True, False)
            self.pic2 = pygame.transform.flip(self.pic2, True, False)
            self.pic3 = pygame.transform.flip(self.pic3, True, False)
            self.dir_flag = True
        elif left and left == self.dir_flag:
            self.pic1 = pygame.transform.flip(self.pic1, True, False)
            self.pic2 = pygame.transform.flip(self.pic2, True, False)
            self.pic3 = pygame.transform.flip(self.pic3, True, False)
            self.dir_flag = False


        # Jump
        if self.rect.bottom < 590 :
            self.yspeed -= 0.8
            self.image = self.pic2
        else:
            self.yspeed = 0
            self.image = self.pic1

        # Movement
        if up == True and self.rect.bottom >=590 and not herodeath:
            self.yspeed = 17
        if right == True and self.rect.bottomright[0] < 800:
            self.rect.x += self.speed
        if left == True and self.rect.bottomleft[0] > 0:
            self.rect.x -= self.speed
        self.rect.y -= self.yspeed

        # Death
        if herodeath:
            self.image = self.pic3
            self.speed = 0