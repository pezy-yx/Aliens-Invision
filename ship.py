import pygame

class Ship():
    '''class of managing ships'''
    
    def __init__(self,ai_game):
        '''initialize the ship and set the primary location'''
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings=ai_game.settings
        
        #load the ship image and obtain the rectangle
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        
        #every new ship is placed at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        
        #store a float number in the attribute x of the ship
        self.x=float(self.rect.x)
        
        #moving flag
        self.moving_right=False
        self.moving_left=False
    
    def update(self):
        '''modify the position of the ship according to moving flag'''
        if self.moving_right:
            self.x+=self.settings.ship_speed
        if self.moving_left:
            self.x-=self.settings.ship_speed
        
        #update rect according to self.x
        self.rect.x=self.x
        
    def blitme(self):
        '''paint the ship at specific location'''
        self.screen.blit(self.image,self.rect)