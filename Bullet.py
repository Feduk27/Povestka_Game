import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_flag):
        pygame.sprite.Sprite.__init__(self)
        self.pic1 = pygame.transform.scale(pygame.image.load('bullet_potato.png').convert_alpha(),(40,50))
        self.image = self.pic1
        self.rect = self.image.get_rect(center=(x, y))
        self.dir_flag = dir_flag


    def update(self):
        if self.dir_flag:
            self.rect.x += 10
        else:
            self.rect.x -= 10
