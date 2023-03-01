import pygame

class background_(pygame.sprite.Sprite):
    def __init__(self, right, left, speed):
        self.image = pygame.image.load('background.jpeg').convert_alpha()
        self.rect = self.image.get_rect()


    def update(self, right, left, speed):
        if left and self.rect.x < 0:
            self.rect.x += speed / 5
        if right and self.rect.x > -400:
            self.rect.x -= speed / 5
