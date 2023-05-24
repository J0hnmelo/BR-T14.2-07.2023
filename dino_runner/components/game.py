import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE,MONTAIN
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        
        self.playing = False
        self.executing = False
        #variaveis back
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        #variaveis score
        self.score = 0
        self.death_count = 0
        #VARIAVEIS NUVENS 
        self.cloud_speed = 5
        self.x_pos_c = 800
        self.y_pos_c = 150
        self.x_pos_c2 = 1750
        self.y_pos_c2 = 50
        self.x_pos_c3 = 330
        self.y_pos_c3 = 0
        self.x_pos_c4 = 550
        self.y_pos_c4 = 120
        self.x_pos_c_s = 1600
        self.y_pos_c_s = 100
        self.x_pos_c2_s = 1200
        self.y_pos_c2_s = 250
        
        #variaveis montain
        self.mont_x = 1900
        self.mont_y = 165
        #variavel hs
        self.high_score = 0
        #variavel vida
        self.life = 3
        
    def execute(self):
        self.executing = True
        while self.executing:
            
            if not self.playing:
                self.display_menu()
        
        pygame.quit()    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True     
        self.reset_game()
    
        while self.playing:
            self.events()
            self.update()
            self.draw()   

    def run2(self):
        if self.life > 0:
            self.playing = True     
            self.continue_game()
    
            while self.playing:
                self.events()
                self.update()
                self.draw()      
        else:
            pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                               
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.update_high_score()
        self.obstacle_manager.update(self)
               
    def update_score(self):
        self.score+=1
        
    def draw_high_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        high_score_text = font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
        high_score_rect = high_score_text.get_rect()
        high_score_rect.center = (1000, 80)
        
        self.screen.blit(high_score_text, high_score_rect)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
    
    def update_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 2
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((23, 23, 23))
        self.draw_background()
        self.draw_simple_cloud()
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        self.cloud_draw_second()
        self.montain_draw()
        self.draw_high_score()
        self.draw_speed()
        pygame.display.flip()

    def display_menu(self):
        if self.death_count == 0:
            self.screen.fill((255, 255, 255))
            x_text_pos = SCREEN_WIDTH//2
            y_text_pos = SCREEN_HEIGHT//2
            
            
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press SPACE to start", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            
            self.screen.blit(text, text_rect)
            print(self.death_count)

        elif self.death_count > 0:
            self.screen.fill((255,255,255))
            x_text_pos = SCREEN_WIDTH//2 - 200
            y_text_pos = SCREEN_HEIGHT//2
            x_text2_pos = SCREEN_WIDTH//2 + 200
            y_text3_pos = SCREEN_HEIGHT//3 
            x_text3_pos = SCREEN_WIDTH//2 
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press R to reset game", True, (0,0,0))
            text2 = font.render("Press C to continue game", True, (0,0,0))
            text3 = font.render(f"You have {self.life} life(s)", True, (0,0,0))
            text_rect = text.get_rect()
            text2_rect = text2.get_rect()
            text3_rect = text3.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            text2_rect.center = (x_text2_pos, y_text_pos)
            text3_rect.center = (x_text3_pos, y_text3_pos)
            self.screen.blit(text, text_rect)
            self.screen.blit(text2, text2_rect)
            self.screen.blit(text3, text3_rect)
            print(self.death_count)
            #self.menu_events_handler()
            #pygame.display.flip()

        self.menu_events_handler()
        pygame.display.flip()
        
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if self.death_count == 0 and event.key == pygame.K_SPACE:
                    self.run()
                elif self.death_count > 0 and event.key == pygame.K_r:
                    self.run()
                elif self.death_count > 0 and event.key == pygame.K_c:
                    self.run2()
                    self.life -= 1
                    if self.life < 0:
                        self.life = 0
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        
        self.screen.blit(text, text_rect)
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_simple_cloud(self):
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
            self.x_pos_c2 = 1750 + 1 * random.randint(100,600)
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

    def montain_draw(self):
        image_M_width = MONTAIN.get_width()
        self.screen.blit(MONTAIN, (self.mont_x, self.mont_y))
        if self.mont_x <= -image_M_width:
            self.screen.blit(MONTAIN, (self.mont_x, self.mont_y))
            self.mont_x = 8000 + 1 * random.randint(300,800)
        self.mont_x -= self.game_speed

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
        self.life = 3
    
    def continue_game(self):
        if self.life > 0:
            self.obstacle_manager.reset_obstacles()
            self.player = Dinosaur()
        else:
            pass
    
    def draw_speed(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        vel_text = font.render(f"Your speed is: {self.game_speed} km/h", True, (255, 255, 255))
        vel_rect = vel_text.get_rect()
        vel_rect.center = (150, 70)
        
        self.screen.blit(vel_text, vel_rect)