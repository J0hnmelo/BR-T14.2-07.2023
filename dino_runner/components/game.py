import pygame
import random
import pygame.mixer
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE,HO_OH, POKE, GO, HEART,DEFAULT_TYPE,BG_SOUND,MENU_SOUND
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
  
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
        self.playing = False
        self.executing = False
        #variaveis back
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        #variaveis score
        self.score = 0
        self.death_count = 0
        #variavel hs
        self.high_score = 0
        #variavel vida
        self.life = 3
        #variaveis hooh
        self.hooh_count = 0
        self.hooh_rect_x = 3000 + random.randint(1000,4000)
        self.hooh_y = 0    
    
    def execute(self):
        self.executing = True
        pygame.mixer.music.load(MENU_SOUND)
        pygame.mixer.music.play(-1)
        while self.executing:
            if not self.playing:
                self.display_menu()
        pygame.quit()    
    
    def run(self):
        self.playing = True     
        self.reset_game()
        pygame.mixer.music.load(BG_SOUND)
        pygame.mixer.music.play(-1)
        while self.playing:
            self.events()
            self.update()
            self.draw()   

    def run2(self):
        if self.life > 0:
            self.playing = True     
            self.continue_game()
            pygame.mixer.music.load(BG_SOUND)
            pygame.mixer.music.play(-1)
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
        self.power_up_manager.update(self)
               
    def update_score(self):
        self.score+=1
        
    def draw_high_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        high_score_text = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))
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
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()  
        self.draw_high_score()
        self.draw_speed()
        self.fly_and_generate_hooh()
        self.draw_life()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000,2)
            
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up Time:{time_to_show}s", True, (255,0,0))
                
                text_rect = text.get_rect()
                text_rect.x = 500
                text_rect.y = 50
                
                self.screen.blit(text, text_rect)
                
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def display_menu(self):
        if self.death_count == 0:
            self.screen.fill((0, 0, 0))
            x_text_pos = SCREEN_WIDTH//2
            y_text_pos = SCREEN_HEIGHT//1.8
            x_logo = SCREEN_WIDTH//8
            y_logo = 0
            
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press SPACE to start", True, (255,255,255))

            text_rect = text.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            self.screen.blit(POKE,(x_logo,y_logo))
            self.screen.blit(text, text_rect)

        elif self.death_count > 0:
            self.screen.fill((0,0,0))
            x_text_pos = SCREEN_WIDTH//2 - 180
            y_text_pos = SCREEN_HEIGHT//1.2
            x_text2_pos = SCREEN_WIDTH//2 + 180
            y_text3_pos = SCREEN_HEIGHT//1.5 
            x_text3_pos = SCREEN_WIDTH//2
            x_over = SCREEN_WIDTH//8
            y_over = 0
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press R to reset game", True, (255,255,255))
            text2 = font.render("Press C to continue game", True, (255,255,255))
            text3 = font.render(f"You have {self.life} life(s)", True, (255,255,255))
            text_rect = text.get_rect()
            text2_rect = text2.get_rect()
            text3_rect = text3.get_rect()
            text_rect.center = (x_text_pos, y_text_pos)
            text2_rect.center = (x_text2_pos, y_text_pos)
            text3_rect.center = (x_text3_pos, y_text3_pos)
            self.screen.blit(GO,(x_over,y_over))
            self.screen.blit(text, text_rect)
            self.screen.blit(text2, text2_rect)
            self.screen.blit(text3, text3_rect)
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
                    if self.life < 0:
                        self.life = 0
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        
        self.screen.blit(text, text_rect)
        
    def draw_life(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f": {self.life}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (400,50)
        self.screen.blit(HEART,(360,35))
        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def fly_and_generate_hooh(self):
        self.image_hooh = HO_OH[self.hooh_count//5]
        self.hooh_rect = self.image_hooh.get_rect()
        self.hooh_count += 1
        if self.hooh_count > 9:
            self.hooh_count = 0
        if self.score > 2000:
            hooh_width = HO_OH[0].get_width()
            self.screen.blit(self.image_hooh,(self.hooh_rect_x,self.hooh_y ))
            if self.hooh_rect_x <= -hooh_width:
                self.score += 1000
                varia_dis = random.randint(1000,2000)
                self.hooh_rect_x = 3000 + varia_dis
                self.screen.blit(self.image_hooh,(self.hooh_rect_x,self.hooh_y ))
            self.hooh_rect_x -= self.game_speed -15

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
        vel_text = font.render(f"Your speed is: {self.game_speed} km/h", True, (0, 0, 0))
        vel_rect = vel_text.get_rect()
        vel_rect.center = (150, 50)
        self.screen.blit(vel_text, vel_rect)