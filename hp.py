import pygame

class HP(pygame.sprite.Sprite):
    def __init__(self, x, count):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('heart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft = (x, 10))
        self.count = 3
    def kill_(self):
        self.kill()

