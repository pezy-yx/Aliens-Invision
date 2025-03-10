import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''a class of managing the bullets the ship shoots out'''
    
    def __init__(self, ai_game):
        '''create a bullet object in the current position of the ship'''
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=ai_game.settings.bullet_color
        
        #create a rectangle representing a bullet and move it to the right place
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        
        #store the bullet's location in float numbers
        self.y=float(self.rect.y)
        
    def update(self):
        '''move the bullet upward'''
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y
        
    def draw_bullet(self):
        '''draw a bullet on the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)