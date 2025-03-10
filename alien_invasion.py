import sys
import pygame
from ship import Ship
from bullet import Bullet
from settings import Settings

class AlienInvasion:
    '''class of managing game resources and behaviors'''
    
    def __init__(self):
        '''initialize the game and create game resources'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        
        #set background color
        self.bg_color=(230,230,230)
        
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,
self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_height=self.screen.get_rect().height
        # self.settings.screen_width=self.screen.get_rect().width
        # pygame.display.set_caption('Alien Invasion')
        
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()

    def run_game(self):
        '''start the main cycle of game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        '''respond to keyboard and mouse events'''
        # listening to keyboard and mouse event
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type==pygame.KEYUP:
                self._check_key_up_events(event)
                
    def _check_key_down_events(self,event):
        '''response to key down'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self,event):
        '''response to key down'''
        if event.key ==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
            
    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        
        #delete those bullets out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        

    def _update_screen(self):
        '''update the image on the screen and switch to a new screen'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
        pygame.display.flip()

if __name__=='__main__':
    #create a game object and run it
    ai=AlienInvasion()
    ai.run_game()