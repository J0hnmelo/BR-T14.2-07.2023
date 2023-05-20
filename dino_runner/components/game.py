import pygame
import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        
        self.playing = False
        #speed background
        self.game_speed = 20
        #speed nuvem
        self.cloud_speed = 5
        #variaveis background
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        ##variaveis das nuvens
        self.x_pos_c = 800
        self.y_pos_c = 150
        self.x_pos_c2 = 1000
        self.y_pos_c2 = 50
        self.x_pos_c3 = 330
        self.y_pos_c3 = 0
        self.x_pos_c4 = 550
        self.y_pos_c4 = 120
        #variaveis das nuvens second
        self.x_pos_c_s = 1600
        self.y_pos_c_s = 100
        self.x_pos_c2_s = 1200
        self.y_pos_c2_s = 250

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 0, 255))
        self.draw_background()
        self.draw_cloud()
        self.cloud_draw_second()
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_c_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_c, self.y_pos_c))
        self.screen.blit(CLOUD, ( self.x_pos_c2, self.y_pos_c2))
        self.screen.blit(CLOUD, ( self.x_pos_c3, self.y_pos_c3))
        self.screen.blit(CLOUD, ( self.x_pos_c4, self.y_pos_c4))
        if self.x_pos_c <= -image_c_width and self.x_pos_c2 <= - image_c_width and self.x_pos_c3 <= -image_c_width and self.x_pos_c4 <= -image_c_width:
            self.screen.blit(CLOUD, (self.x_pos_c, self.y_pos_c))
            self.screen.blit(CLOUD, ( self.x_pos_c2, self.y_pos_c2))
            self.screen.blit(CLOUD, ( self.x_pos_c3, self.y_pos_c3))
            self.screen.blit(CLOUD, ( self.x_pos_c4, self.y_pos_c4))
            self.x_pos_c = 1100 + 1 * random.randint(100,600)
            self.y_pos_c = 200 + 1 * random.randint(-100, 70)
            self.x_pos_c2 = 1300 + 1 * random.randint(100,600)
            self.y_pos_c2 = 110 + 1 * random.randint(-100, 70)
            self.x_pos_c3 = 1400 + 1 * random.randint(100,600)
            self.y_pos_c3 =  280 + 1 * random.randint(-130,10)
            self.x_pos_c4 = 1600 + 1 * random.randint(100,600)
            
        self.x_pos_c -= self.cloud_speed
        self.x_pos_c2 -= self.cloud_speed 
        self.x_pos_c3 -= self.cloud_speed 
        self.x_pos_c4 -= self.cloud_speed 

    def cloud_draw_second(self):
        image_c_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_c_s, self.y_pos_c_s))
        self.screen.blit(CLOUD, (self.x_pos_c2_s, self.y_pos_c2_s))
        if self.x_pos_c_s <= -image_c_width and self.x_pos_c2_s <= - image_c_width :
            self.screen.blit(CLOUD, (self.x_pos_c_s, self.y_pos_c_s))
            self.screen.blit(CLOUD, (self.x_pos_c2_s, self.y_pos_c2_s))
            self.x_pos_c_s = 1100 + 1 * random.randint(100,600)
            self.y_pos_c_s = 200 + 1 * random.randint(-100, 70)
            self.x_pos_c2_s = 1300 + 1 * random.randint(100,600)
            self.y_pos_c2_s = 110 + 1 * random.randint(-100, 70)

            
        self.x_pos_c_s -= self.cloud_speed
        self.x_pos_c2_s -= self.cloud_speed 

