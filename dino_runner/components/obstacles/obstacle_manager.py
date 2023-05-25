import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.dragon import Dragon
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, DRAGON,GO_SOUND


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            option = random.randint(1,4)
            if option == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS[random.randint(0,2)]))
            elif option == 2:
                cactus = Cactus(LARGE_CACTUS[random.randint(0,2)])
                cactus.rect.y = 377# mudando a posição do cactus Largo
                self.obstacles.append(cactus)
            elif option == 3:
                self.obstacles.append(Bird(BIRD))
            elif option == 4:
                self.obstacles.append(Dragon(DRAGON))
         
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    pygame.mixer.music.load(GO_SOUND)
                    pygame.mixer.music.play(-1)
                    game.life -=1
                else:
                    self.obstacles.remove(obstacle)
                
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles.clear()