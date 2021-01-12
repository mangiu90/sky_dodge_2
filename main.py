import pygame

from pygame.locals import *
from SceneBase import *
from inicio import *


class StartScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == KEYDOWN and event.key == K_RETURN:
                
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        bg_start = pygame.image.load( PATH + "img/start.png").convert()
        bg_start.set_colorkey((255, 255, 255), RLEACCEL)
        screen.blit(bg_start, [50, 400])

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))

run_game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS_NUMBER, StartScene())


