import pygame
import random

class RunnerSprite(pygame.sprite.Sprite) :
    
    def __init__(self, imageFile):
        super().__init__()
        
        self.image = pygame.image.load(str(imageFile))
        self.rect = self.image.get_rect()
        
    def moveWithMouse(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self, speed):
        self.rect.x -= speed
    
    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def update(self, screenWidth, screenHeight):
        if self.rect.x <= - self.rect.width:
            self.rect.x = screenWidth
            self.rect.y = random.randint(0, screenHeight - self.rect.height)
    