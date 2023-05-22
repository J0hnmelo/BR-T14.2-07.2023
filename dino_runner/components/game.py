import pygame
import pygame.font
import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, BIRD,MONTAIN, LARGE_CACTUS, SMALL_CACTUS, RUNNING
from dino_runner.components.dinosaur import Dinosaur


#LEMBRETES: 1 - CRIAR UMA CLASS PRAS NUVENS FICARIA MAIS SIMPLES 
#           2 - CRIAR UM DICIONARIO PARA AS NUVENS VAI FICAR MAIS SIMPLES 
#           3 - CRIAR UMA CLASS PRA CADA COISA FICA MAIS SIMPLES 


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.points = 0
        self.death_points = 0
        self.player = Dinosaur()
        self.fonte = pygame.font.Font('RobotoCondensed-Regular.ttf', 20)
        self.playing = False
        #speed background
        self.game_speed = 15
        #speed nuvem
        self.cloud_speed = 5
        #variaveis background
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        ##variaveis das nuvens
        self.x_pos_c = 800
        self.y_pos_c = 150
        self.x_pos_c2 = 1750
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
        ##variaveis do bird

        #self.image_bird = BIRD[0] #estado inicial

        self.bird_rect_x = 3000
        self.bird_count = 0
        self.bird_y = 310
        self.bird_rect_x_rec = 3050
        self.bird_y_rec = 330
        ##variaveis montanha
        self.mont_x = 1900
        self.mont_y = 165
        #variaveis do small cactus
       
        self.image_s_cactust0 = SMALL_CACTUS[0]
        self.image_s_cactust0_rect = self.image_s_cactust0.get_rect()
        self.cactus0_x = 2000
        self.cactus0_x_rec = 2020
        self.cactus0_y = 320
        self.cactus0_y_rec = 350
        self.image_s_cactust1 = SMALL_CACTUS[1]
        self.image_s_cactust1_rect = self.image_s_cactust1.get_rect()
        self.cactus1_x = 4000
        self.cactus1_x_rec = 4035
        self.cactus1_y = 320
        self.cactus1_y_rec = 357
        self.image_s_cactust2 = SMALL_CACTUS[2]
        self.image_s_cactust2_rect = self.image_s_cactust2.get_rect()
        self.cactus2_x = 5000
        self.cactus2_x_rect = 5050
        self.cactus2_y = 320
        self.cactus2_y_rect = 357
        self.image_s_cactust0_w = self.image_s_cactust0.get_width()
        self.image_s_cactust1_w = self.image_s_cactust1.get_width()
        self.image_s_cactust2_w = self.image_s_cactust2.get_width()

        ##LARGE cactus variaveis
        self.image_l_cactust0 = LARGE_CACTUS[0]
        self.image_l_cactust0_rect = self.image_l_cactust0.get_rect()
        self.cactus0_xl = 1200
        self.cactus0_xl_rect = 1225
        self.cactus0_yl = 300
        self.cactus0_yl_rect = 347
        self.image_l_cactust1 = LARGE_CACTUS[1]
        self.image_l_cactust1_rect = self.image_l_cactust1.get_rect()
        self.cactus1_xl = 5000
        self.cactus1_xl_rect = 5048
        self.cactus1_yl = 300
        self.cactus1_yl_rect = 345
        self.image_l_cactust2 = LARGE_CACTUS[2]
        self.image_l_cactust2_rect = self.image_l_cactust2.get_rect()
        self.cactus2_xl = 6000
        self.cactus2_xl_rect = 6050
        self.cactus2_yl = 300
        self.cactus2_yl_rect = 345
        self.image_l_cactust0_w = self.image_l_cactust0.get_width()
        self.image_l_cactust1_w = self.image_l_cactust1.get_width()
        self.image_l_cactust2_w = self.image_l_cactust2.get_width()

        #self.play= True

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
        self.fly_and_generate_bird()
        self.score()
       # if self.play == False:
            #self.reset_game()
           # self.play = True
        if self.player.dino_rect.colliderect(self.bird_rect) or self.player.dino_rect.colliderect(self.image_s_cactust0_rect) or self.player.dino_rect.colliderect(self.image_s_cactust1_rect) or self.player.dino_rect.colliderect(self.image_s_cactust2_rect) or self.player.dino_rect.colliderect(self.image_l_cactust0_rect) or self.player.dino_rect.colliderect(self.image_l_cactust1_rect) or self.player.dino_rect.colliderect(self.image_l_cactust2_rect):
            pygame.time.delay(1000)
            #self.death_points += 1
            #self.menu().run = False
            #self.menu(death_points = 0)
            #self.play = False
            self.playing = False
    '''
    def menu(self, death_points = 0):
        run = True
        while run:
            self.screen.fill((255,255,255))
            self.fonte2 = pygame.font.Font('RobotoCondensed-Regular.ttf', 30)

            if self.death_points == 0:
                self.text2 = self.fonte2.render("Press ENTER to start", True, (0,0,0))
            elif self.death_points > 0:
                self.text2 = self.fonte2.render("Press ENTER to restart", True, (0,0,0))
                self.scorePoints = self.fonte2.render("Your score:" + str(self.points), True, (0,0,0))
                self.scoreRect = self.scorePoints.get_rect()
                self.scoreRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
                self.screen.blit(self.scorePoints, self.scoreRect)
            self.textRect = self.text2.get_rect()
            self.textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            self.screen.blit(self.text2, self.textRect)
            self.screen.blit(RUNNING[0], (SCREEN_WIDTH //2 - 20, SCREEN_HEIGHT // 2 -140))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.playing = False

                if event.type == pygame.KEYDOWN:
                    self.run()
        '''

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((25, 25, 25))
        self.draw_background()
        self.draw_cloud()
        self.cloud_draw_second()
        self.fly_and_generate_bird()
        if self.points > 600:
            self.generete_large_cactus()
        self.generete_small_cactus()
        self.montain_draw()
        self.player.draw(self.screen)
        self.score()
        self.dino_rect_create = pygame.draw.rect(self.screen, (255,0,0), self.player.dino_rect, 2)

        pygame.display.flip()

    '''
    def reset_game(self):
        self.draw()
        self.points = 0
        self.death_points = 0
        self.player = Dinosaur()
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
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
        self.bird_rect_x = 3000
        self.bird_count = 0
        self.bird_y = 310
        self.bird_rect_x_rec = 3050
        self.bird_y_rec = 330
        self.mont_x = 1900
        self.mont_y = 165
        self.cactus0_x = 2000
        self.cactus0_x_rec = 2020
        self.cactus0_y = 320
        self.cactus0_y_rec = 350
        self.cactus1_x = 4000
        self.cactus1_x_rec = 4035
        self.cactus1_y = 320
        self.cactus1_y_rec = 357
        self.cactus2_x = 5000
        self.cactus2_x_rect = 5050
        self.cactus2_y = 320
        self.cactus2_y_rect = 357
        # ...
        self.playing = True
    '''




    def draw_background(self):##reconstruir fazendo um dicionario
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed









    def draw_cloud(self):##reconstruir fazendo um dicionario
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






    
    def fly_and_generate_bird(self):
        self.image_bird = BIRD[self.bird_count//3]
        self.bird_rect = self.image_bird.get_rect()
        self.bird_count += 1
        if self.bird_count > 5:
            self.bird_count = 0
        if self.points > 600:
            bird_width = BIRD[0].get_width()
            self.screen.blit(self.image_bird,(self.bird_rect_x,self.bird_y ))
            self.bird_rect.center = (self.bird_rect_x_rec, self.bird_y_rec)
            if self.bird_rect_x <= -bird_width:
                varia_y = random.randint(-80,10)
                
                self.bird_y = 310 + varia_y
                self.bird_y_rec = 330 + varia_y
                self.bird_rect_x = 3000 
                self.bird_rect_x_rec = 3050 
                self.screen.blit(self.image_bird,(self.bird_rect_x,self.bird_y ))
                self.bird_rect.center = (self.bird_rect_x_rec, self.bird_y_rec)
            self.bird_rect_x -= self.game_speed -10 
            self.bird_rect_x_rec -= self.game_speed -10
 


    def generete_small_cactus(self):
        self.screen.blit(self.image_s_cactust0,(self.cactus0_x,self.cactus0_y ))
        self.image_s_cactust0_rect.center = (self.cactus0_x_rec,self.cactus0_y_rec)
        self.screen.blit(self.image_s_cactust1,(self.cactus1_x,self.cactus1_y ))
        self.image_s_cactust1_rect.center = (self.cactus1_x_rec,self.cactus1_y_rec)
        self.screen.blit(self.image_s_cactust2,(self.cactus2_x,self.cactus2_y ))
        self.image_s_cactust2_rect.center = (self.cactus2_x_rect,self.cactus2_y_rect)
        if self.cactus2_x <= -self.image_s_cactust2_w:
            varia_x_0 = random.randint(-500,1000)
            varia_x_1 = random.randint(-1500,1000)
            varia_x_2 = random.randint(-500,1000)
            self.cactus0_x = 4000 + varia_x_0
            self.cactus0_x_rec = 4020 + varia_x_0 
            self.cactus1_x = 5000 + varia_x_1
            self.cactus1_x_rec = 5035 + varia_x_1
            self.cactus2_x = 7000 + varia_x_2
            self.cactus2_x_rect = 7050 + varia_x_2
            self.screen.blit(self.image_s_cactust0,(self.cactus0_x,self.cactus0_y ))
            self.image_s_cactust0_rect.center = (self.cactus0_x_rec,self.cactus0_y_rec)
            self.screen.blit(self.image_s_cactust1,(self.cactus1_x,self.cactus1_y ))
            self.image_s_cactust1_rect.center = (self.cactus1_x_rec,self.cactus1_y_rec)
            self.screen.blit(self.image_s_cactust2,(self.cactus2_x,self.cactus2_y ))
            self.image_s_cactust2_rect.center = (self.cactus2_x_rect,self.cactus2_y_rect)
        self.cactus0_x -= self.game_speed
        self.cactus0_x_rec -= self.game_speed
        self.cactus1_x -= self.game_speed
        self.cactus1_x_rec -= self.game_speed
        self.cactus2_x -= self.game_speed
        self.cactus2_x_rect -= self.game_speed


    
    def generete_large_cactus(self):
        self.screen.blit(self.image_l_cactust0,(self.cactus0_xl,self.cactus0_yl ))
        self.image_l_cactust0_rect.center = (self.cactus0_xl_rect,self.cactus0_yl_rect)
        self.screen.blit(self.image_l_cactust1,(self.cactus1_xl,self.cactus1_yl ))
        self.image_l_cactust1_rect.center = (self.cactus1_xl_rect,self.cactus1_yl_rect)
        self.screen.blit(self.image_l_cactust2,(self.cactus2_xl,self.cactus2_yl ))
        self.image_l_cactust2_rect.center = (self.cactus2_xl_rect,self.cactus2_yl_rect)
        if self.cactus2_xl <= -self.image_l_cactust2_w:
            varia0_xl = random.randint(-500,1000)
            varia1_xl = random.randint(-1500,1000)
            varia2_xl = random.randint(-500,1000)
            self.cactus0_xl = 2000 + varia0_xl
            self.cactus0_xl_rect = 2025 + varia0_xl
            self.cactus1_xl = 8000 + varia1_xl
            self.cactus1_xl_rect = 8048 + varia1_xl
            self.cactus2_xl = 9000 + varia2_xl
            self.cactus2_xl_rect = 9050 + varia2_xl
            self.screen.blit(self.image_l_cactust0,(self.cactus0_xl,self.cactus0_yl ))
            self.image_l_cactust0_rect.center = (self.cactus0_xl_rect,self.cactus0_yl_rect)
            self.screen.blit(self.image_l_cactust1,(self.cactus1_xl,self.cactus1_yl ))
            self.image_l_cactust1_rect.center = (self.cactus1_xl_rect,self.cactus1_yl_rect)
            self.screen.blit(self.image_l_cactust2,(self.cactus2_xl,self.cactus2_yl ))
            self.image_l_cactust2_rect.center = (self.cactus2_xl_rect,self.cactus2_yl_rect)
            
        self.cactus0_xl -= self.game_speed
        self.cactus0_xl_rect -= self.game_speed
        self.cactus1_xl -= self.game_speed
        self.cactus1_xl_rect -= self.game_speed
        self.cactus2_xl -= self.game_speed
        self.cactus2_xl_rect -= self.game_speed
    



    def montain_draw(self):
        image_M_width = MONTAIN.get_width()
        self.screen.blit(MONTAIN, (self.mont_x, self.mont_y))
        if self.mont_x <= -image_M_width:
            self.screen.blit(MONTAIN, (self.mont_x, self.mont_y))
            self.mont_x = 8000 + 1 * random.randint(300,800)
        self.mont_x -= self.game_speed






    def score(self):
        
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text = self.fonte.render("Points: " + str(self.points), True,(255,255,255))
        text_rect = text.get_rect()
        text_rect_center = (900,40)
        self.screen.blit(text, text_rect_center)

   


