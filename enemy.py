import pygame

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Voenkom.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (75,125))
        self.rect = self.image.get_rect(midbottom = (x, 590))
        self.add(group)
    def update(self, x):
        if self.rect.centerx - x != 0:
            enemyxspeed = (-self.rect.centerx + x) // 100
            if enemyxspeed == 0:
                enemyxspeed = 1
        else:
            enemyxspeed = 0
        self.rect.x += enemyxspeed
    def kill_(self):
        self.kill()