import pygame

from pygame.locals import *
from SceneBase import *
from inicio import PATH
from Sprites import *

class StartScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        bg_start = pygame.image.load( PATH + "img/start.png").convert()
        bg_start.set_colorkey((255, 255, 255), RLEACCEL)
        screen.blit(bg_start, [400, 100])

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.background_image = pygame.image.load(PATH + "img/sky.jpg").convert()
        pygame.mixer.music.load(PATH + "sound/Apoxode_-_Electric_1.mp3")
        pygame.mixer.music.play(loops=-1)
        self.move_up_sound = pygame.mixer.Sound(PATH + "sound/Rising_putter.ogg")
        self.move_down_sound = pygame.mixer.Sound(PATH + "sound/Falling_putter.ogg")
        self.collision_sound = pygame.mixer.Sound(PATH + "sound/Collision.ogg")

        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 250)
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1000)

        self.player = Player()

        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == self.ADDENEMY:
                self.new_enemy = Enemy()
                self.enemies.add(self.new_enemy)
                self.all_sprites.add(self.new_enemy)

            elif event.type == self.ADDCLOUD:
                self.new_cloud = Cloud()
                self.clouds.add(self.new_cloud)
                self.all_sprites.add(self.new_cloud)

            elif event.type == KEYDOWN and event.key == K_SPACE:
                while True: 
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_SPACE:
                        break 
                
        self.player.update(pressed_keys, self.move_up_sound, self.move_down_sound)

        self.enemies.update()
        self.clouds.update()

    def Update(self):
        pass
    
    def Render(self, screen):
        screen.blit(self.background_image, [0, 0])

        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.kill()
            self.move_up_sound.stop()
            self.move_down_sound.stop()
            self.collision_sound.play()
            self.SwitchToScene(StartScene())

        
